### 问题描述：
***
给定2D数组，判断是否是Toeplitz数组。如果从左上角到右下角的每个对角线都有相同的元素，那么矩阵就是Toeplitz。
### 代码实现：
***
```python
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        count = 0 # 记录对角线元素List个数是否正确（M + N - 1）
        M = len(matrix) # 行数
        N = len(matrix[0]) # 列数

        # 向量右上三角
        for column in range(N):# 控制list个数
            templist = []
            m = 0
            n = column
            while m < M and n < N:
                templist.append(matrix[m][n])
                m += 1
                n += 1
            # print (templist)
            # 判断对角线元素是否相等
            if max(templist) != min(templist):
                return False
            count += 1

        # 左下三角形
        for row in range(1, M):
            templist = []
            m = row
            n = 0
            while m < M and n < N:
                templist.append(matrix[m][n])
                m += 1
                n += 1
            # print (templist)
            # 判断对角线元素是否相等
            if max(templist) != min(templist):
                return False
            count += 1

        if count != M + N - 1:
            return False
        else:
            return True
```
### 总结：
***
1. 思路：将对角线上的元素提出，组成临时列表，判断列表元素是否相等。将矩阵分成两块，右上角三角形和左下角三角形，分别抽出对角线元素判断是否相等。之所以分成两块，是因为右上由列数控制临时列表个数，左下由行数控制列表个数。每个临时列表元素个数由行和列下标同时控制，即行和列达到最大值时，临时列表停止填装元素。
