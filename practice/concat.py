# -*-coding:utf-8-*-
"""
实现两张3通道图片的拼接
"""

import os
import numpy as np
import tensorflow as tf
import argparse

IMAGE_TYPE = [".jpg", ".png"]


# 拼接图片
def combine(be_dir, af_dir, so_dir):
    if not os.path.exists(be_dir):
        raise Exception("missing image paths -- be_dir")

    if not os.path.exists(af_dir):
        raise Exception("missing image paths -- af_dir")

    if not os.path.exists(so_dir):
        os.mkdir(so_dir)

    be_paths = os.listdir(be_dir)
    # print be_paths
    # bee_paths = glob(be_dir+"/*.png")
    # print (bee_paths)
    count = 0
    with tf.Session() as sess:

        for ele in be_paths:
            if os.path.isdir(os.path.join(be_dir, ele)):
                continue
            count += 1
            name, _ = os.path.splitext(os.path.basename(ele))
            # print ("concating image %s" % name)

            #  获取源域图片
            or_img_path = os.path.join(be_dir, ele)

            if not os.path.exists(or_img_path):
                raise Exception("original image is gown.")

            or_img = load(or_img_path, sess)
            # print (or_img)

            #  寻找目的域同名（不同类型）图片
            for ext in IMAGE_TYPE:
                join_path = os.path.join(af_dir, name+ext)
                if os.path.exists(join_path):
                    be_img = load(join_path, sess)
                    break
            else:
                raise Exception("%s is not existing in %s" % (name, af_dir))

            # 判断源域图片与目的域图片的大小
            if or_img.shape != be_img.shape:
                raise Exception("different sizes.")

            # 拼接图像
            concat_image = np.concatenate([or_img, be_img], axis=1)
            concat_image_path = os.path.join(so_dir, ele)
            save(concat_image, concat_image_path, sess, count, True)

        print ("Processing is down!")


# 加载图片
def load(path, sess):
    _, ext = os.path.splitext(path)
    with open(path, "rb") as f:
        content = f.read()  # 2进制
        # print (content)

    if ext == ".jpg":
        img = tf.image.decode_jpeg(content)
    elif ext == ".png":
        img = decode_png_my(content, sess)
    else:
        raise Exception("there is no suitable image type.")

    return to_float(img, sess)


# 解码图片  unit-8
def decode_png_my(imge_real, sess):
    #  创建通道
    image = tf.placeholder(tf.string)
    img_deco = tf.image.decode_png(contents=image)
    #  喂入数据
    img = sess.run(img_deco, feed_dict={image: imge_real})

    return img


def decode_jpg_my(imge_real, sess):
    image = tf.placeholder(tf.string)
    img_deco = tf.image.decode_jpeg(contents=image)
    img = sess.run(img_deco, feed_dict={image: imge_real})
    return img


#  转float
def to_float(img, sess):
    image = tf.placeholder(tf.uint8)
    to_float = tf.image.convert_image_dtype(image, dtype=tf.float32)
    image_to_float = sess.run(to_float, feed_dict={image: img})
    return image_to_float


#  保存图片
def save(image, path, sess, count, replace=False):
    img = to_unit8(image, sess)
    _, ext = os.path.splitext(path)
    if ext == ".jpg":
        img = encode_jpg_my(img, sess)
    elif ext == ".png":
        img = encode_png_my(img, sess)
    else:
        raise Exception("there is no suitable image type.")

    if os.path.exists(path):
        if replace:
            os.remove(path)
        else:
            print ("%s already exist." % os.path.basename(path))

    with open(path, "wb") as f:
        f.write(img)

    print ("saving image %s------ %s" % (count, os.path.basename(path)))


# 转unit8
def to_unit8(img, sess):
    image = tf.placeholder(dtype=tf.float32)
    image_to_unit = tf.image.convert_image_dtype(image, dtype=tf.uint8)
    unit_image = sess.run(image_to_unit, feed_dict={image: img})
    return unit_image


# 编码图片
def encode_png_my(img, sess):
    image = tf.placeholder(dtype=tf.uint8)
    img_en = tf.image.encode_png(image)
    img_en = sess.run(img_en, feed_dict={image: img})
    return img_en


def encode_jpg_my(img, sess):
    image = tf.placeholder(dtype=tf.uint8)
    img_en = tf.image.encode_jpeg(image)
    img_en = sess.run(img_en, feed_dict={image: img})
    return img_en



aa = "/media/hry/udata/underwater_relative/data/clean_real"
bb = "/media/hry/udata/underwater_relative/data/unclean_fake"
cc = "/media/hry/udata/underwater_relative/data/testpix/concat_image"


if __name__ == '__main__':
    os.environ["CUDA-VISIBLE-DEVICES"] = "0"
    args = argparse.ArgumentParser()
    # args.add_argument("--source_one_dir", type=str, required=True, help="one of the images path which need to be concat")
    # args.add_argument("--source_two_dir", type=str, required=True, help="one of the images path which need to be concat")
    # args.add_argument("--purpose_dir", type=str, required=True, help="saving concat images")
    args.add_argument("--source_one_dir", type=str, default=aa, help="saving concat images")
    args.add_argument("--source_two_dir", type=str, default=bb, help="saving concat images")
    args.add_argument("--purpose_dir", type=str, default=cc, help="saving concat images")
    a = args.parse_args()
    combine(a.source_one_dir, a.source_two_dir, a.purpose_dir)

