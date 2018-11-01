# -*-coding:utf-8-*-
"""
#  读取tfrecord文件
#  tf.train.string_input_producer读取tfrecords文件的list建立FIFO序列，
可以申明num_epoches和shuffle参数表示需要读取数据的次数（不设置epoches参数，则无限读取数据）以及时候将tfrecords文件读入顺序打乱，
然后定义TFRecordReader读取上面的序列返回下一个record，
用tf.parse_single_example对读取到TFRecords文件进行解码，
根据保存的serialize example和feature字典返回feature所对应的值。
此时获得的值都是string，需要进一步解码（decode）为所需的数据类型。
把图像数据的string reshape成原始图像后可以进行preprocessing操作。
此外，还可以通过tf.train.batch或者tf.train.shuffle_batch将图像生成batch序列。

由于tf.train函数会在graph中增加tf.train.QueueRunner类，
而这些类有一系列的enqueue选项使一个队列在一个线程里运行。
为了填充队列就需要用tf.train.start_queue_runners来为所有graph中的queue runner启动线程，
而为了管理这些线程就需要一个tf.train.Coordinator来在合适的时候终止这些线程
"""

import argparse as arg
import os
import tensorflow as tf

IN_TYPE = ".tfrecords"
aa = "/media/hry/udata/candelete_test/anime.tfrecords"

args = arg.ArgumentParser()
args.add_argument("--input_dir", type=str, default=aa, help="tfRecord file")
args.add_argument("--epoch", type=int, default=100, help="running epoch")
args.add_argument("--batch_size", type=int, default=10, help="batch_size")
args.add_argument("--image_height", type=int, default=96, help="image original height or resize height")
args.add_argument("--image_width", type=int, default=96, help="image original width or resize width")
args.add_argument("--envir", type=str, default="0", help="gpu number")
a = args.parse_args()


class Reader(object):

    def __init__(self, tfrecord_dir, image_size_h, image_size_w, batch_size=1, min_queue_examples=800, num_threads=1, num_epoch=100):
        self.tfrecord_dir = tfrecord_dir
        self.image_height = image_size_h
        self.image_width = image_size_w
        self.batch_size = batch_size
        self.min_queue_examples = min_queue_examples
        self.num_threads = num_threads
        self.reader = tf.TFRecordReader()
        self.num_epoch = num_epoch

    def read_data(self):
        _, ext = os.path.splitext(self.tfrecord_dir)
        if ext != IN_TYPE:
            raise Exception("the input file is not tfrecord type")

        # 生成 队列
        filename_queue = tf.train.string_input_producer([self.tfrecord_dir], num_epochs=self.num_epoch)
        #  读取数据
        _, serialized_example = self.reader.read(filename_queue)
        #  对读取到TFRecords文件进行解码
        features = tf.parse_single_example(
            serialized_example,
            features={
                "image_name": tf.FixedLenFeature([], tf.string),
                "encoded_image": tf.FixedLenFeature([], tf.string)
            })
        image_name = features["image_name"]
        image_batch = tf.image.decode_jpeg(contents=features["encoded_image"], channels=3)
        image_batch = self._pre_process(image_batch)
        # create bathch
        image_batch = tf.train.shuffle_batch([image_batch], batch_size=self.batch_size, num_threads=self.num_threads,
                                             capacity=self.min_queue_examples + 3 * self.batch_size,
                                             min_after_dequeue=self.min_queue_examples)

        return image_batch, image_name

    def _pre_process(self, image):
        image_resize = tf.image.resize_images(image, size=[self.image_height, self.image_width])   # 装载batch前， 必须resize shape!!!!

        # Transfrom from int image ([0,255]) to float tensor ([-1.,1.])
        image_to_float = tf.image.convert_image_dtype(image_resize, dtype=tf.float32)

        return (image_to_float/127.5)-1.0  # (image+1.0)/2.0


if __name__ == '__main__':
    path = os.path.dirname(aa)
    os.environ["CUDA_VISIBLE_DEVICES"] = a.envir
    reader1 = Reader(aa, a.image_height, a.image_height, batch_size=a.batch_size, num_epoch=a.epoch)
    images_batch, name = reader1.read_data()
    with tf.Session() as sess:

        init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
        sess.run(init_op)

        # 创建线程管理器，管理在Session中启动的所有线程
        coord = tf.train.Coordinator()
        # 启动QueueRunner, 此时文件名队列已经进队
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        try:
            step = 0
            while not coord.should_stop():
                data = sess.run([images_batch, name])
                print (data[0].shape)
                #####################################################
                # 操作
                #####################################################
                step += 1
                print ("=" * 20, step)

        except KeyboardInterrupt:
            print ("KeyboardInterrupt")
            coord.request_stop()
        except Exception as e:
            coord.request_stop(e)
        finally:
            coord.request_stop()
            coord.join(threads=threads)





