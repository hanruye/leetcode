```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset#load数据集

# 引入数据集(209个训练样本，50个测试样本)
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
# 获取训练样本及测试样本个数，图片像素
m_train = train_set_x_orig.shape[0]
m_test = test_set_x_orig.shape[0]
num_px = train_set_x_orig.shape[1]
# 将训练及测试样本转换成需要的矩阵{由（209,64,64,3）至（12288，209）}
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
# 标准化数据
train_set_x = train_set_x_flatten/255.
test_set_x = test_set_x_flatten/255.


# σ()函数
def sigmoid(z):
    return 1/(1+np.exp(-z))


# 初始化权值w和阈值b
def init_with_zeros(dim):
    w = np.random.randn(dim, 1) * 0.01
    assert (w.shape == (dim, 1))
    b = 0
    assert (isinstance(b, float) or isinstance(b, int))
    return w, b


# 计算前向传播、反向传播参数
def propagation(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(np.dot(w.T, X) + b)
    lost = -(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    cost = np.sum(lost)/m
    dz = A - Y
    db = np.sum(dz)/m
    dw = np.dot(X, dz.T)/m
    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())
    grades = {"dw": dw, "db": db}
    return grades, cost


# 模拟梯度下降
def optimize(w, b, X, Y, num_iterations, learning_rate, print_cast = False):
    costs = []
    for i in range(num_iterations):
        grads, cost = propagation(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w = w - learning_rate * dw
        b = b - learning_rate * db
        if i % 100 == 0:
            costs.append(cost)
        if print_cast and i % 100 == 0:
            print ("Cost after interation %i: %f" % (i, float(cost)))
    params = {"w": w, "b": b}
    grads = {"dw": dw, "db": db}
    return params, grads, costs


# 预测模块
def prediction(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(np.dot(w.T, X) + b)
    for i in range(A.shape[1]):
        if A[0, i] <= 0.5:
            Y_prediction[0, i] = 0
        else:
            Y_prediction[0, i] = 1
    assert (Y_prediction.shape == (1, m))
    return Y_prediction


# 整合形成辨识猫图片的模型
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.01, print_cost=True):
    w, b = init_with_zeros(X_train.shape[0])

    parameters, grads, costs11 = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    w = parameters["w"]
    b = parameters["b"]

    Y_prediction_test = prediction(w, b, X_test)
    Y_prediction_train = prediction(w, b, X_train)

    print("train accuracy:{} %".format(np.mean(np.abs(Y_prediction_train - Y_train))))
    print("test accuracy:{} %".format(np.mean(np.abs(Y_prediction_test - Y_test))))

    d = {"costs": costs11,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": learning_rate,
         "num_iterations": num_iterations}
    return d

```
