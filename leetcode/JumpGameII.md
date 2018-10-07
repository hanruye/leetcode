### 问题描述：
***
给定一个非负整数数组，您首先被定位在数组的第一个索引处。数组中的每个元素表示该位置的最大跳转长度。
你的目标是在最小跳跃次数中达到最后一个数。
### python实现：
***
```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump, curEnd, curFastpoint = 0, 0, 0
        for i in range(len(nums)-1):
            curFastpoint = max(curFastpoint, i+nums[i])
            if i == curEnd:
                jump += 1
                curEnd = curFastpoint

        return jump
```
### 总结：
***
1. 思路：每次跳跃的范围是[index，index+nums[index]],找到跳转范围中跳跃的最远点fastPoint,当当前点到达跳跃范围 curEnd = index+nums[index] 点时，进行下一次跳跃。
