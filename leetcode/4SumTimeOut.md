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
        if not nums or len(nums) < 4: return []
        nums = sorted(nums)
        results_list = []
        l = len(nums)
        for i in range(l-3):
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3])>target:break
            for j in range(i+1, l-2):
                if (nums[i] + nums[j] + nums[j + 1] + nums[j+2])>target: break
                for p in range(j+1, l-1):
                    if (nums[i] + nums[j] + nums[p] + nums[p+1])>target: break
                    temp_list = self.remove_repeat(nums[p+1:l])
                    # 符合a+b+c+d = target 要求
                    if (target - nums[i] - nums[j] - nums[p]) in temp_list:
                        half_right = [nums[i], nums[j], nums[p], target - nums[i] - nums[j] - nums[p]]
                        flag = True
                        # 判断新数组是否已包含于结果中，不存在则存储
                        for ele in results_list:
                            if self.is_eq(ele, half_right):
                                flag = False
                                break
                        if flag: results_list.append(half_right)


        return results_list
    
    # 判断两个List是否相同，同返回True
    def is_eq(self, l1, l2):
        return op.eq(sorted(l1), sorted(l2))
    
    # list元素去重后升序
    def remove_repeat(self, li):
        if not li:return []
        return list(set(li))
        #return sorted(list(set(li)))

    

```
### 总结：
***
1. 思路：升序数组;3重循环控制前3个元素，每重循环第1条条件语句作用是判断当前重循环是否有必要执行;第4个可能元素组成升序去重数组，判断是否符合条件。