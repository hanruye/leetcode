import tensorflow as tf
import os

"""
# 使用装饰器方式包装方法
"""


def create_op(func, **placeholder):
    print(placeholder)
    op = func(**placeholder)

    def inner(**kwargs):
        feed_dic = dict()
        for name, value in kwargs.items():
            placeholder_id = placeholder[name]
            feed_dic[placeholder_id] = value
        return tf.get_default_session().run(op, feed_dict=feed_dic)
    return inner


# 类型转换
uint8_to_float32 = create_op(
    tf.image.convert_image_dtype,
    image=tf.placeholder(dtype=tf.uint8),
    dtype=tf.float32)

float32_to_uint8 = create_op(
    tf.image.convert_image_dtype,
    image=tf.placeholder(dtype=tf.float32),
    dtype=tf.uint8
)

# 解码
decode_jpeg = create_op(
    tf.image.decode_jpeg,
    contents=tf.placeholder(dtype=tf.string)
)

decode_png = create_op(
    tf.image.decode_png,
    contents=tf.placeholder(dtype=tf.string)
)

# 编码
encode_jpeg = create_op(
    tf.image.encode_jpeg,
    image=tf.placeholder(dtype=tf.uint8)
)

encode_png = create_op(
    tf.image.encode_png,
    image=tf.placeholder(dtype=tf.uint8)
)


def load_and_save(input_path, output_dir):
    if not os.path.exists(image_path):
        raise Exception("...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    paths = os.listdir(input_path)
    _, ext = os.path.splitext(paths[1])
    in_path = os.path.join(input_path, paths[1])
    out_path = os.path.join(output_dir, paths[1])

    with open(in_path, "rb") as read:
        content = read.read()

    if ".jpg" == ext:
        image_uint8 = decode_jpeg(contents=content)
    elif ".png" == ext:
        image_uint8 = decode_png(contents=content)
    else:
        raise Exception(".................")

    image_float32 = uint8_to_float32(image=image_uint8)
    image_uint8 = float32_to_uint8(image=image_float32)

    if ".jpg" == ext:
        image_string = encode_jpeg(image=image_uint8)
    elif ".png" == ext:
        image_string = encode_png(image=image_uint8)
    else:
        raise Exception(".................")

    with open(out_path, "wb") as writer:
        writer.write(image_string)


init_op = tf.global_variables_initializer()
image_path = "/media/hry/ubuntu/candelete/bing/"
image_path_out = "/media/hry/ubuntu/candelete/bing_copy/"


with tf.Session() as sess:
    sess.run(init_op)
    image_float = load_and_save(image_path, image_path_out)

