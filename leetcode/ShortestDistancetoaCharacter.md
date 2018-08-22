### 问题描述：
***
给定字符串S和字符C，找出每个字符串元素与字符C最短的距离。
### 代码实现：
***
```python
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        integerInt = [] # 存放最小距离
        cindex = [] #  存放元素c的全部位置

        # 找出S中全部的C元素位置
        for i in range(len(S)):
            if S[i] == C:
                cindex.append(i)
        # 找出每个元素距离C的最小值
        for j in range(len(S)):
            templist = []
            for k in cindex:
                templist.append(abs(j - k))
            integerInt.append(min(templist))

        return integerInt

```
### 总结：
***
1. 思路：先找出全部字符C在字符串S中的位置，再遍历S中每个元素与字符C的最短距离