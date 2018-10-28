# -*-coding:utf-8-*-
"""
创建tfrecord文件,
no image resize
"""


import tensorflow as tf
import os
try:
    from scandir import scandir
except ImportError:
    from os import scandir

import argparse as arg
import random
import time
import math


OUT_TYPE = ".tfrecords"
IMAGE_TYPE = [".jpg", ".png"]

#aa = "/media/hry/udata/u_sys_data/code_info/data/datas/bing"
#bb = "/media/hry/udata/candelete_test/bingtest.tfrecords"

parse = arg.ArgumentParser()
parse.add_argument("--input_dir", type=str, required=True, help="the images path")
parse.add_argument("--output_dir", type=str, required=True, help="the images path")
a = parse.parse_args()


# 存储tfRecord数据
def save_data(input_dir, output_dir):
    if not os.path.exists(input_dir):
        raise Exception("need input direction")

    # 生成路径
    if not os.path.exists(os.path.dirname(output_dir)):
        os.makedirs(os.path.dirname(output_dir))
    # 确认正确存储格式
    _, ext = os.path.splitext(output_dir)
    if ext != OUT_TYPE:
        raise Exception("output file is not tfRecords type")

    # 读取数据
    image_path_list = data_reader(input_dir, True)
    # print (data_reader(input_dir, True))
    # 写入tfrecords文件
    with tf.python_io.TFRecordWriter(output_dir) as writer:
        num_path = len(image_path_list)

        for i in range(num_path):
            with tf.gfile.FastGFile(image_path_list[i], "rb") as f:
                image_buffer = f.read()

            example = _convert_to_example(image_path_list[i], image_buffer)
            writer.write(example.SerializeToString())

            if i % 100 == 0:
                print ("processing %s %s" % (i, num_path))


# 将图像信息转成example
def _convert_to_example(image_path, image_buffer):
    basename = os.path.basename(image_path)

    example = tf.train.Example(features=tf.train.Features(feature={
        "image_name": _bytes_to_feature(tf.compat.as_bytes(basename)),
        "encoded_image": _bytes_to_feature(image_buffer)

    }))
    return example


# 将byteList转成特征类型
def _bytes_to_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


# 装载图片路径
def data_reader(input_dir, shuffle=False):
    if not os.path.exists(input_dir):
        raise Exception("input direction can't ne connected. ")

    # 循环装载图片路径
    image_path = list()
    name_list = os.listdir(input_dir)
    for image_name in name_list:
        img_pth = os.path.join(input_dir, image_name)
        if os.path.isfile(img_pth):
            _, ext = os.path.splitext(image_name)
            if ext.lower() in IMAGE_TYPE:
                image_path.append(img_pth)
            else:
                print ("%s is unsuitable image type, and is throwed" % image_name)
                continue
        else:
            continue
    print ("the number of input images is %s" % len(image_path))
    print (image_path)
    # 随机打乱顺序
    if shuffle:
        shuffled_number = list(range(len(image_path)))
        random.seed(math.ceil(time.time()))
        random.shuffle(shuffled_number)
        image_path = [image_path[i] for i in shuffled_number]

    return image_path


if __name__ == '__main__':
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    aa = a.input_dir
    bb = a.output_dir
    save_data(aa, bb)

