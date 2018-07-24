### 问题描述：
***
实现数数并说序列：1, 11, 21, 1211, 111221, ...
```python
class Solution:
    def countAndSay(self, num):
        """
        :type n: int
        :rtype: str
        """
        value = "1"
        count = 1
        for i in range(1, num):
            tempvalue = ""
            for j in range(len(value)):
                if j < len(value) - 1 and value[j] == value[j+1]:
                    count += 1
                else:
                    tempvalue += str(count) + str(value[j])
                    count = 1
            value = tempvalue
        return value
```
