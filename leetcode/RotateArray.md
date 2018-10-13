### 问题描述
***
给定一个数组，将数组向右旋转k步，其中k是非负的。
### 代码实现
***
```python
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)  # 控制循环反转次数，取余的原因：k次效果和k+len(nums) 效果一样
        def rotate_by_index(temp_list, be, af):
            while be < af:
                tem_num = temp_list[af]
                temp_list[af] = temp_list[be]
                temp_list[be] = tem_num
                be += 1
                af -= 1

        rotate_by_index(nums, 0, len(nums)-1)  # 整个数组反转 
        rotate_by_index(nums, 0, k-1)  # 前K个元素反转
        rotate_by_index(nums, k, len(nums)-1)  # 后L-K个元素反转 

```
### 总结：
***
1. 方法体内套方法体，类操作。
