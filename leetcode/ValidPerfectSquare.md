### 问题描述：
***
给定一个正整数num，如果num是完全平方否则为False，就写一个返回True的函数。
### 代码实现：
***
```python
import math as ma
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, end = 0, ma.ceil(num/2.0)
        print(end)
        while left <= end:
            mid = left + (end - left) // 2
            if mid ** 2 > num : end = mid-1
            elif mid ** 2 < num : left = mid+1
            else:return True
        return False
```