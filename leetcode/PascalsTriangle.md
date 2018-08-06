### 问题描述：
***
给定整数a,生成Pascal三角形
### 代码实现：
***
```python
class Solution(object):
    def generate(self, rownums):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        List = []
        if rownums == 0:
            return List
        if rownums == 1:
            List.append([1])
            return List
        if rownums == 2:
            List.append([1])
            List.append([1, 1])
            return List
        if rownums > 2:
            List.append([1])
            List.append([1, 1])
            for i in range(3, rownums+1):
                temp_list=[]
                temp_list.append(1)
                for j in range(1, len(List[i-2])):
                    a = List[i-2]
                    b = List[i-2][j]
                    temp_list.append(List[i-2][j-1]+List[i-2][j])
                temp_list.append(1)
                List.append(temp_list)
            return List

```
### 思路：
***
1. 第一层和第二层无特殊规律，特定预处理。从第三层开始，每行两端的值为1,其余元素的值为对应肩膀上的上层元素和，即：a[i][j] = a[i-1][j-1]+a[i-1][j].外层循环控制行数，内层循环控制每行元素个数。