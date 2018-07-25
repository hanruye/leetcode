### 问题描述
***
给定数组，找出子数组中值和最大值。
### 代码实现
***
```python
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # out limited time
        tempdic = []
        for i in range(len(nums)):
            value = nums[i]
            tempvalue = value
            for j in range(i+1, len(nums)):
                value += nums[j]
                if tempvalue < value:
                    tempvalue = value
            tempdic.append(tempvalue)
        tempdic.sort()
        return tempdic.pop()
        """
        tempvalue = nums[0]
        maxvalue = nums[0]
        for value in nums[1:]:
            if tempvalue < 0:
                tempvalue = value
            else:
                tempvalue += value
            if tempvalue > maxvalue:
                maxvalue = tempvalue

        return maxvalue
```
### 总结
***
1. 思路：初始化临时值为数组首值，遍历数组，若临时值>0,临时值加上当前值，若临时值<0，则将当前值赋值给临时值（因为此时，临时值+当前值<当前值），从当前值位置起重新记值。