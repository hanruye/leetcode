### 问题描述：
***
给定字符串（内容由‘(){}[]’随机组成），判断各个元素是否配对出现，例如"{{}[]}()"，"()[]{}"等满足条件，"([}]{"不满足条件
```python
class Solution:
    def isValid(self, str):
        """
        :type s: str
        :rtype: bool
        """
        stack, dic = [], {"(": ")", "[": "]", "{": "}"}
        for s in str:
            if s in dic.keys():
                stack.append(s)
            else:
                if stack:
                    if dic[stack.pop()] != s:
                        return False
                else:
                    return False
        return not stack
```
### 总结
***
思路：括号配对按就近配对原则。遍历字符串，若第i位是左括号，将此位暂存至列表中;若第i位是右括号，将临时列表中的最后一位取出，判断是否配对，若配对继续遍历，不配对退出遍历。
