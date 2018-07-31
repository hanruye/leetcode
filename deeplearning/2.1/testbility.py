#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import base
from testCases import *


# 初始化权值和阈值
def init_param(lay_limits):
    parames = {}
    L = len(lay_limits)

    for l in range(1, L-1):
        parames["W" + str(l)] = np.random.randn(lay_limits[l], lay_limits[l-1])*2/np.sqrt(lay_limits[l-1])
        parames["b" + str(l)] = np.zeros((lay_limits[l], 1))

    parames["W" + str(L-1)] = np.random.randn(lay_limits[-1], lay_limits[-2]) * 1 / np.sqrt(lay_limits[-2])
    parames["b" + str(L-1)] = np.zeros((lay_limits[-1], 1))

    assert (parames["W" + str(L-1)].shape == (lay_limits[-1], lay_limits[-2]))
    assert (parames["b" + str(L-1)].shape == (lay_limits[-1], 1))
    return parames


# 普通前向传播
def activation_forward(X, parameters):
    L = len(parameters)//2
    caches = []
    A = X
    for i in range(0, L-1):
        A_pre = A
        A, cache = linear_activation_forward(A_pre, parameters["W"+str(i+1)], parameters["b"+str(i+1)], base.RelU)
        caches.append(cache)
    A_pre = A
    AL, cache = linear_activation_forward(A_pre, parameters["W"+str(L)], parameters["b"+str(L)], base.Sigmoid)
    caches.append(cache)
    assert (AL.shape == (parameters["W"+str(L)].shape[0], X.shape[1]))
    caches.append(AL)
    return AL, caches


# 单层
def linear_activation_forward(A_pre, W, b, status):
    Z = np.dot(W, A_pre) + b
    if status == base.RelU:
        A = relu(Z)
    elif status == base.Sigmoid:
        A = sigmoid(Z)
    assert (Z.shape == (W.shape[0], A_pre.shape[1]))
    assert (A.shape == Z.shape)
    cache = (A_pre, W, b, Z)
    return A, cache



# RelU
def relu(value):
    a = np.maximum(0, value)
    assert (value.shape == a.shape)
    return a


# Sigmoid
def sigmoid(z):
    a = 1/(1+np.exp(-z))
    assert (z.shape == a.shape)
    return a


# 含随dropout正则化的前向传播
def activation_forward_dropout(X, parameters, keep_prob):
    L = len(parameters) // 2
    caches = []
    A = X
    for l in range(1, L):
        A_pre = A
        A, cache = linear_activation_forward(A_pre, parameters["W" + str(l)], parameters["b" + str(l)],
                                             base.RelU)
        ##############################
        D = np.random.randn(A.shape[0], A.shape[1])
        D = D < keep_prob
        A = np.multiply(A, D)
        A /= keep_prob
        ##############################
        cadche = (cache, D)
        caches.append(cadche)
    A_pre = A
    AL, cache = linear_activation_forward(A_pre, parameters["W" + str(L)], parameters["b" + str(L)], base.Sigmoid)
    caches.append(cache)
    caches.append(AL)

    return AL, caches


# 计算普通成本
def compute_cost(AL, Y):
    m = Y.shape[1]
    cost = (1. / m) * (-np.dot(Y, np.log(AL).T) - np.dot(1 - Y, np.log(1 - AL).T))

    cost = np.squeeze(cost)  # To make sure your cost's shape is what we expect (e.g. this turns [[17]] into 17).
    assert (cost.shape == ())

    return cost


# 带L2正则化的成本
def compute_cost_with_regularization(AL, Y, parameters, lambd=0):
    m = Y.shape[1]
    L = len(parameters)//2 # 获取网络层数
    cost = compute_cost(AL, Y)
    L2_cost = 0
    #####################################
    for i in range(1, L+1):
        L2_cost += np.sum(np.square(parameters["W"+str(i)]))
    L2_cost = L2_cost * (lambd/(2*m))
    #####################################
    assert (L2_cost.shape == ())
    cost = cost + L2_cost

    return cost


# 普通反向传播
def linear_backward(dZ, cache):
    A_pre, W, b, Z = cache
    m = A_pre.shape[1]

    dW = np.dot(dZ, A_pre.T)/m
    db = np.sum(dZ, axis=1, keepdims=True)/m
    dA_pre = np.dot(W.T, dZ)

    return dA_pre, dW, db


def activation_backward(X, Y, caches):
    grades = {}
    m = X.shape[1]
    L = len(caches)-1
    cachess = caches[0:L]
    AL = caches[-1]
    Y = Y.reshape(AL.shape)
    assert (Y.shape == AL.shape)

    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
    current_cache = cachess[L - 1]
    dZ = sigmoid_back(dAL, cachess[L-1][-1])

    grades["dA" + str(L - 1)], grades["dW" + str(L)], grades["db" + str(L)] = linear_backward(dZ, current_cache)
    for l in reversed(range(L-1)):
        current_cache = cachess[l]
        dZ = relu_back(grades["dA" + str(l+1)], cachess[l][-1])
        dA_prev_temp, dW_temp, db_temp = linear_backward(dZ, current_cache)
        grades["dA" + str(l)] = dA_prev_temp
        grades["dW" + str(l + 1)] = dW_temp
        grades["db" + str(l + 1)] = db_temp

    return grades


def backward_propagation_with_regularization(X, Y, caches, lambd):
    m = X.shape[1]
    grades = activation_backward(X, Y, caches)
    L = len(caches) - 1
    cachess = caches[0:L]
    a = len(grades)//3
    b = len(cachess)
    assert (len(grades)//3 == len(cachess))

    for i in range(len(cachess)):
        grades["dW" + str(i + 1)] += (lambd/m)*cachess[i][1]

    return grades


def backward_propagation_with_dropout(X, Y, cachess, keep_prob):
    m = X.shape[1]

    caches_s = []
    for i in range(len(cachess) - 2):
        caches_s.append(cachess[i][0])
    caches_s.append(cachess[-2])
    caches_s.append(cachess[-1])
    caches_s = tuple(caches_s)
    grades = activation_backward(X, Y, caches_s)

    for j in range(len(grades)//3-1):
        grades["dA"+str(j+1)] = np.multiply(grades["dA"+str(j+1)], cachess[j][1])
        grades["dA" + str(j + 1)] /= keep_prob

    return grades


def relu_back(dA, cache):
    Z = cache
    dZ = np.array(dA, copy=True)  # just converting dz to a correct object.

    # When z <= 0, you should set dz to 0 as well.
    dZ[Z <= 0] = 0

    assert (dZ.shape == Z.shape)

    return dZ


def sigmoid_back(dA, cache):
    Z = cache

    s = 1 / (1 + np.exp(-Z))
    dZ = dA * s * (1 - s)

    assert (dZ.shape == Z.shape)

    return dZ


def update_parameters(parameters, grads, learning_rate):
    L = len(parameters)//2
    for l in range(1, L):
        parameters["W"+str(l)] -= learning_rate*grads["dW"+str(l)]
        parameters["b"+str(l)] -= learning_rate*grads["db"+str(l)]
    return parameters


def predict(X, y, parameters):
    """
    This function is used to predict the results of a  n-layer neural network.

    Arguments:
    X -- data set of examples you would like to label
    parameters -- parameters of the trained model

    Returns:
    p -- predictions for the given dataset X
    """

    m = X.shape[1]
    p = np.zeros((1, m), dtype=np.int)

    # Forward propagation
    a3, caches = activation_forward(X, parameters)

    # convert probas to 0/1 predictions
    for i in range(0, a3.shape[1]):
        if a3[0, i] > 0.5:
            p[0, i] = 1
        else:
            p[0, i] = 0

    # print results

    # print ("predictions: " + str(p[0,:]))
    # print ("true labels: " + str(y[0,:]))
    print("Accuracy: " + str(np.mean((p[0, :] == y[0, :]))))

    return p
