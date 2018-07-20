### 问题描述
***
给定罗马数字，按照对应关系转换成整数

### 代码实现
***
```python
class Solution:
    def romanToInt(self, rmoanum):
        """
        :type s: str
        :rtype: int
        """
        romandic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
                "CD": 400, "CM": 900}
        strlen = len(rmoanum)
        result = 0
        i = 0
        while i < strlen:
            if (i < strlen - 1):
                if (rmoanum[i] + rmoanum[i + 1] in romandic):
                    result += romandic[rmoanum[i] + rmoanum[i + 1]]
                    i += 2
                else:
                    result += romandic[rmoanum[i]]
                    i += 1
            else:
                result += romandic[rmoanum[i]]
                i += 1
        return result
```
### 总结
***
1. python代码块用缩进区别。
2. 思路：遍历字符串查找字典中对应的key，根据key对应的value值计算。首先拼接i位和i+1位，判断字典中是否存在该key，若存在获取对应value,step = 2 继续遍历;若不存在，直接判断获取第i位的value值，step = 1 继续遍历