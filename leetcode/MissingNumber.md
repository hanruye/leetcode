### 问题描述：
***
给定一个包含n个不同数字的数组，从0,1,2，…， n，找到数组中缺失的那个。
### 代码实现：
***
```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sortedlist = sorted(nums)
        maxnum = sortedlist[-1]
        temp = [i for i in range(maxnum + 1)]
        if sum(temp) - sum(nums) == 0:
            if sortedlist[0] != 0:
                return 0
            else:
                return maxnum + 1
        return sum(temp) - sum(nums)
```
### 总结：
***
1. 思路：找到列表中最大数值N，以次数值N为最大值新建一个从0到N的列表tempList，两个列表元素求和再作差，即可得到缺失的数值。