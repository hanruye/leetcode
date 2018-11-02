# -*-coding:utf-8-*-
"""
生成html文件
"""
import dominate
from dominate.tags import *
import os


class HTML(object):
    def __init__(self, web_dir, title_name, refresh=0):
        self.web_dir = web_dir
        self.title_name = title_name
        self.images_dir = self.web_dir + "/images"
        self.make_dir = self.make_dirs()

        self.table = table(border=0, style="table-layout: fixed;")

        self.doc = dominate.document(title=self.title_name)
        # 网页刷新时间（秒计算）
        if refresh > 0:
            with self.doc.head:
                meta(http_equiv="refresh", content=str(refresh))

    def make_dirs(self):
        flag = True
        try:
            if not os.path.exists(self.web_dir):
                os.makedirs(self.web_dir)
            if not os.path.exists(self.images_dir):
                os.makedirs(self.images_dir)
        except:
            flag = False

        return flag

    #  向dom元素中拼接图片信息
    def add_image(self, images_src, num_tr=3, num_td=2):  # num_tr 行数 num_td 列数
        if not self.make_dirs():
            raise Exception("there is no dirs.")
        # print (self.table)
        image_path = os.listdir(images_src)

        self.doc.add(self.table)  # 填充table 元素
        with self.table:
            tr_i = 0
            while tr_i < num_tr:
                with tr():
                    for j in range(num_td):
                        if tr_i*num_td + j >= len(image_path):
                            tr_i = num_tr
                            break
                        with td(style="word-wrap: break-word;", halign="center", valign="top"):
                            with a(href=os.path.join("images", image_path[tr_i * num_td + j])):
                                img(src=os.path.join("images", image_path[tr_i * num_td + j]))
                    # print (self.table)

                tr_i += 1

    # 保存数据
    def save_html(self):
        save_path = os.path.join(self.web_dir, "index.html")
        with open(save_path, "wt") as f:
            f.write(self.doc.render())


if __name__ == '__main__':
    h = HTML("web", "test_html", refresh=10)
    h.add_image(h.images_dir, num_tr=1, num_td=3)
    h.save_html()
