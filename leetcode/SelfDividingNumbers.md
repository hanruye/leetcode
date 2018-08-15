### 问题描述：
***
给定整数范围的最小最大值，找出在此范围内所有的自除数。自除数：能被本数各个位置上的数整除。
### 代码实现：
***
```python
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        divnum = []
        isdivi = True
        while left <= right:
            tempstr = str(left)
            # 判断是否包含0
            if str(0) in tempstr:
                left += 1
                continue
            #  遍历临时字符串，判断是否是diving num
            for i in range(len(tempstr)):
                if left % int(tempstr[i]) != 0:
                    isdivi = False
                    break
            if isdivi:
                divnum.append(left)

            left += 1
            isdivi = True

        return divnum
```
### 总结：
***
1. 思路：判定是否包含0,若不包含，则判别能否被各个元素整除。将数字转成字符串，便于取出整数各个位置上的元素。