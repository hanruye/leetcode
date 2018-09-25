### 问题描述：
***
给定一个非负整数c，你的任务是确定是否有两个整数a和b使a^2 + b^2 = c。
### 代码实现：
***
```python
import math as ma
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0:return True
        cc = int (ma.ceil(ma.sqrt(c)))
        for i in range(cc):
            a = i ** 2
            b = c - a
            if b < a:return False
            aa = ma.sqrt(b)
            if aa == int(aa):return True
        return False
```