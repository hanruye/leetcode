### 题目：
***
给定一个数组数为n个整数和一个整数目标，在数字中找到三个整数，使和最接近目标。返回三个整数的和。假设每个输入都只有一个解决方案。
### python实现：
***
```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        new_array = []
        l = len(nums)
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    new_array.append(nums[i]+nums[j]+nums[k])

        tem = [ele - target for ele in new_array]
        minnum = min([abs(ele) for ele in tem])
        num = [ele for ele in tem if abs(ele) == minnum]

        return num[0]+target

        """
        new_array = []# 存放3元素和
        l = len(nums)
        for i in range(l-2):# 控制第1个元素大小
            for j in range(i+1, l-1): # 控制第2个元素大小
                for k in range(j+1, l): # 控制第3个元素大小
                    if not new_array: new_array.append(nums[i]+nums[j]+nums[k])
                    if abs(new_array[-1] - target) == 0: return target
                    if abs(new_array[-1] - target) > abs(nums[i]+nums[j]+nums[k] - target):
                        new_array[-1] = nums[i]+nums[j]+nums[k]

        return new_array[0]

```
### 总结：
***
1. 思路：3重循环控制遍历3个元素，找最小差值。