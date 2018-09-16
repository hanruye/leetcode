### 问题描述：
***
我们正在玩猜谜游戏。游戏内容如下:
我从1到n选一个数，你必须猜出我选了哪个数。
每次你猜错了，我就告诉你数字是高还是低。
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
### 代码实现：
***
```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin, end, middle = 1, n, n//2
        while guess(middle) != 0:
            if guess(middle) == 1:
                end = middle
                middle = middle//2
            elif guess(middle) == -1:
                begin = middle
                middle = begin + (end - begin) // 2
        
        return middle
```
### 总结：
***
1. 思路：将数组中间分成前后两个字数组，2分查找。