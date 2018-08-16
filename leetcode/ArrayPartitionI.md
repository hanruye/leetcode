### 问题描述：
***
给定偶元素个数的数组，元素两两配对后选择其中较小的值求和，问如何配对才能返回最大值。
### 代码实现：
***
```python
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  重新排序
        nums.sort()
        summ = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                summ += nums[i]
        return summ
```
### 总结：
***
1. 思路：即要求单个元素最小又要求全部元素和最大。直接升序，选择偶数下标的元素求和。