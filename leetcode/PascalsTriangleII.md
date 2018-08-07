### 问题描述：
***
给定整数a, 以列表形式返回Pascal三角形的第a+1行元素
### 代码实现：
***
```python
class Solution(object):
    def getRow(self, rownums):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rownums == 0:
            return [1]
        if rownums == 1:
            return [1, 1]

        stack = []
        if rownums > 1:
            stack.append([1, 1])
            count = 1
            while stack:
                count += 1
                now_list = [1]
                pre_list = stack.pop()
                for i in range(len(pre_list)-1):
                    now_list.append(pre_list[i]+pre_list[i+1])
                now_list.append(1)
                stack.append(now_list)
                if count >= rownums:
                    break
            return stack.pop()
```
### 总结：
***
1. 思路：使用列表暂存上一层元素，当前层列表两端元素为1,其他元素全为对应肩膀上的元素和。