### 问题描述：
***
爬楼梯问题，给定楼梯阶数，每次行走1阶或2阶梯，问共有多少种方法走完阶梯。
### 代码实现：
***
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """递归方法超出时间
        total = 0 # 行走方式
        if n <= 2: # 递归终止条件（最后剩余1个台阶，只有1种行走方式，剩余2个台阶，则有2种行走方式）
            total = n
        else:
            total = Solution().climbStairs(n-1) + Solution().climbStairs(n-2) #  每次行走都有两种行走方式：1步或2步
        return total
        """
        if n < 3:
            return n
        else:
            pre_pre_step = 1
            pre_step = 2
            for i in range(3, n+1):
                nstep = pre_pre_step + pre_step
                pre_pre_step = pre_step
                pre_step = nstep
            return pre_step


```
### 总结：
***
1. 思路：第I个台阶的行走方式是第I-1和I-2的方式和。