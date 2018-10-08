### 问题描述：
***
给定一个数组数字，编写一个函数将所有0移动到它的末尾，同时保持非零元素的相对顺序。
### python实现：
***
```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = 0
        # 将数组中非0元素按位置关系提到数组前部
        for ele in nums:
            if ele != 0:
                nums[index] = ele
                index += 1
        # 将0元素归至数组末端
        while index < len(nums):
            nums[index] = 0
            index += 1
            
        print nums

```
### 总结：
***
1. 思路：将非0元素集中提至数组前端，剩余位置全部填0。