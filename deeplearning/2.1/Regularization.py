#!/usr/bin/python
# -*- coding: UTF-8 -*-


import numpy as np
import matplotlib.pylab as plt
from reg_utils import sigmoid,plot_decision_boundary,initialize_parameters,load_2D_dataset,predict_dec
from reg_utils import compute_cost,predict_dec,forward_propagation,backward_propagation,update_parameters
import sklearn
import sklearn.datasets
import scipy.io
from testCases import *
from testbility import *


plt.rcParams['figure.figsize'] = (7.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'


train_X, train_Y, test_X, test_Y = load_2D_dataset()

# plt.show()


def model(X, Y, learning_rate = 0.3, num_iterations = 30000, print_cost = True, lambd = 0, keep_prob = 0.9):
    grads = {}
    costs = []
    m = X.shape[1]
    layers_dims = [X.shape[0], 20, 3, 1]
    # 初始化参数
    parameters = init_param(layers_dims)
    # 循环查找最优权值和阈值LINEAR -> RELU -> LINEAR -> RELU -> LINEAR -> SIGMOID.
    caches = 0
    for i in range(0, num_iterations):
        # 非正则化
        if keep_prob == 1:
            AL, caches = activation_forward(X, parameters)
        elif keep_prob < 1:
            AL, caches = activation_forward_dropout(X, parameters, keep_prob)

        # 计算成本
        if lambd == 0:
            cost = compute_cost(AL, Y)
        else:
            cost = compute_cost_with_regularization(AL, Y, parameters, lambd)

        # 这里确保L2和dropout正则化只使用一个，事实上两种可以同时使用
        assert (lambd == 0 or keep_prob == 1)
        if lambd == 0 and keep_prob == 1:
            grads = activation_backward(X, Y, caches)
        elif lambd != 0:
            grads = backward_propagation_with_regularization(X, Y, caches, lambd)
        elif keep_prob < 1:
            grads = backward_propagation_with_dropout(X, Y, caches, keep_prob)

        parameters = update_parameters(parameters, grads, learning_rate)

        # Print the loss every 10000 iterations
        if print_cost and i % 1000 == 0:
            print("Cost after iteration {}: {}".format(i, cost))
        if print_cost and i % 1000 == 0:
            costs.append(cost)

    # plot the cost
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (x1,000)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    return parameters


parameters = model(train_X, train_Y)
print ("On the training set:")
predictions_train = predict(train_X, train_Y, parameters)
print ("On the test set:")
predictions_test = predict(test_X, test_Y, parameters)

plt.title("Model without regularization")
axes = plt.gca()
axes.set_xlim([-0.75, 0.40])
axes.set_ylim([-0.75, 0.65])
plot_decision_boundary(lambda x: predict_dec(parameters, x.T), train_X, train_Y)
