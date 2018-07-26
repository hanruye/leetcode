### 问题描述：
***
给定整数列表，末位加1，返回新列表。例子：给定[9, 9],返回[1, 0, 0]
### 代码实现：
***
```python
class Solution(object):
    def plusOne(self, nums):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dic = []
        leni = len(nums)
        nums[leni - 1] += 1#尾位+1
        summ = 0
        for i in range(0, leni):
            summ = summ * 10 + nums[i]
            
        while summ > 0:
            dic.append(int(summ % 10))
            summ = summ/10
            
        sss = dic[::-1]#切片倒序
        return sss

        
```

### 总结：
***
1. 思路：直接忽略加1后进位问题，列表最后位加1后，循环列表组成对应整数，最后再按位拼接成新的列表。