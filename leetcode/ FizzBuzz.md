### 问题描述：
***
给定正整数，返回字符串列表，返回规则：“Fizz”代表仅是3的倍数的整数，“Buzz”代表仅是5的倍数的整数，“FizzBuzz”代表既是3的倍数又是5的倍数的整数，其他数字仅改变类型。
### 代码实现：
***
```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        templist = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                templist.append("FizzBuzz")
            elif i % 3 == 0:
                templist.append("Fizz")
            elif i % 5 == 0:
                templist.append("Buzz")
            else:
                templist.append(str(i))

        return templist


```