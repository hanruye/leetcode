### 问题描述：
***
给定未排序的整数数组，找出数组元素内两两最大差值。
### 代码实现：
***
```python
class Solution(object):
    def maximumGap(self, nums):
        nums = sorted(nums)
        if len(nums) < 2:return 0
        templist = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
        return max(templist)
```
### 总结：
***
1. 对数组升序，对升序后的数组元素，两两计算差值，找出最大差值