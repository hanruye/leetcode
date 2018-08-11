
### 问题描述：
***
给定两个十进制整数，判断其二进制对应位元素不想等的个数
### 代码实现：
***
```python
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0

        strx = self.get_b(x)
        stry = self.get_b(y)
        lendif = len(strx) - len(stry)
        str0 = ""
        # 长度小的前面补0
        for i in range(abs(lendif)):
            str0 += str(0)
        alllen = len(strx)
        if lendif > 0:
            stry = str0 + stry
        if lendif < 0:
            strx = str0 + strx
            alllen = len(stry)

        for j in range(alllen):
            if strx[j] != stry[j]:
                count += 1

        return count
    # 将十进制转换成二进制字符串
    def get_b(self, num):
        tempStr = ""
        while num:
            tempStr += str(num % 2)
            num = num // 2
        return tempStr[::-1]
```
### 总结：
***
1. 思路：先将十进制转换乘二进制字符串，比较长度前面补0,逐位判断元素是否相等。