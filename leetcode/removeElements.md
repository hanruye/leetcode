###  问题描述：
***
去除列表nums中的特定值a，空间消耗只有O(1)

```python
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                index += 1
                if i is not index:
                    # O(0)交换位置
                    nums[i] = nums[i] ^ nums[index]
                    nums[index] = nums[i] ^ nums[index]
                    nums[i] = nums[i] ^ nums[index]
        return index+1
```
###  总结：
***
1. 思路：循环列表元素与给定数字对比，若不相等,将该元素放与数组index+1位的元素对换。
