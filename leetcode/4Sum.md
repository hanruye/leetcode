### 题目：
***
给定一个n个整数的数组数和一个整数目标，在数字中是否有a、b、c和d元素使a + b + c + d =目标?在数组中查找所有唯一的四联体，它给出目标的和。
### python实现：
***
```python
import operator as op
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
       
        res = set()# 集合存储结果
        nums = sorted(nums)
        for i in range(len(nums)-3):# 控制第1个元素
            for j in range(i+1, len(nums)-2):# 控制第2个元素
                head = j+1
                tail = len(nums)-1
                # 第3第4元素通过两头查找剩余元素的方法，减少1层循环
                while head < tail:
                    temp_sum = nums[i] + nums[j] + nums[head] + nums[tail]
                    if temp_sum == target:
                        res.add(tuple(sorted([nums[i], nums[j], nums[head], nums[tail]])))
                        head += 1
                        tail -= 1
                    elif temp_sum < target:
                        head += 1
                    else:
                        tail -= 1

        return list(res)
```
