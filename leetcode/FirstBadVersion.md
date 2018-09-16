### 问题描述：
***
您是一名产品经理，目前正领导一个团队开发新产品。不幸的是，你们最新版本的产品质量检测不合格。由于每个版本都是基于上一个版本开发的，所以在一个坏版本之后的所有版本都是坏的。假设有n个版本[1,2，…]你想找出第一个坏的，它会导致下面所有的坏。
### 代码实现：
***
```python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not isBadVersion(n):return 0 # 第1个就是坏的
        if isBadVersion(1):return 1 # 全部是好的
        begin, end, middle= 1, n, n//2 
        while True:
            if isBadVersion(middle):# 中间的版本坏的
                end = middle
                middle = middle//2
                if end == middle:return middle+1
            else:
                begin = middle
                middle = begin+(end-middle)//2
                if begin == middle:return middle+1
```
### 总结：
***
1. 思路：将数组中间分成前后两个字数组，2分查找。