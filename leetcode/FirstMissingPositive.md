### 题目：
***
给定一个未排序的整数数组，查找丢失的最小正整数。
### python实现：
***
```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 数组长度代表连续正整数最小值的最大可能（例如：长度为4的数组，丢失的最小正整数范围是1～4）
        l = len(nums)

        # 将数组中所有非正整数设定为 长度+100(只要比数组长度大就可以)
        for i in range(l):
            if nums[i] <= 0:nums[i] = l+100
        # 逐个判断元素值是否大于数组长度(查找满足条件的较小正整数)
        for i in range(l):
            if abs(nums[i]) <= l: nums[n-1] = - abs(nums[n-1])# 满足最小正整数范围，则剔除
        # 找到最小缺失值
        for i in range(l):
            if nums[i] > 0:
                return i+1

        return l+1
```
### 总结：
***
1. 思路：用数组下标代表最小正整数范围。先将数组元素的非正整数剔除（剔除条件：元素值小于等于0的，重新赋值），重新遍历数组，判断元素值是否在最小正整数范围内，若在，则以当前元素值为下标，元素值取反剔除;最后遍历数组，找到最小缺失值。