### 问题描述：
***
给定一个已按升序排序的整数数组，找到两个数字，使它们相加得到一个特定的目标数字。
### 代码实现：
***

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {} #  存放元素：位置
        for i in range(len(numbers)):
            n = numbers[i]
            m = target - n
            if m in temp:
                return [temp[m] + 1, i + 1]
            temp[n] = i

        return None
```
### 总结：
***
1. no loop
2. 思路：利用字典键的唯一性。