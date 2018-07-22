### 问题描述
***
给定已升序数组，返回数组中非重复数的个数，并在原有数组内将非重复数重新排序，要求只允许使用一个额外变量，即空间消耗只有O(1)

### 代码实现
***
```python
class Solution:
    def removeDuplicates(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        if len(num) < 2:
            return len(num)
        for i in range(1, len(num)):
            if num[i] > num[index]:
                index += 1
                # O(0)交换位置
                if index is not i:
                    num[i] = num[i] + num[index]
                    num[index] = num[i] - num[index]
                    num[i] = num[i] - num[index]
        # print(num)
        return index + 1

```
### 总结：
***
1. in-place 算法：原地算法，使用特定数目额外空间进行原数据转换的算法。
2. 思路：初始时以第一个元素为非重复基准位，记录下标（index = 0）;循环列表第1至最后一位，若第i位元素比基准位元素大，交换第i位元素与基准位下一位元素（即index+1），重新记录基准位。