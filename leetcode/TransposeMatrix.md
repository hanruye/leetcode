### 问题描述：
***
给定数组，返回该数组的转置
### 代码实现：
***
```python
class Solution(object):
    def transpose(self, AList):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        tempList = []
        for ele in AList[0]:
            tempList.append([ele])
        for i in range(1, len(AList)):# 控制行
            for j in range(len(AList[i])):# 控制列
                tempList[j].append(AList[i][j])

        return tempList
```
### 总结：
***
1. 思路：数组的行转列，第1行转第1列，第2行转第2列......