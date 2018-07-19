### 问题描述：
***
给定字符串数组，找字符串数组中最长的公共前缀字符串。
### 代码实现
***
```python
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strlen = 0
        strstr = ""
        strslen = len(strs)
        if 1 == strslen:
            return strs[strslen-1]
        else:
            # 找到列表中最短字符串的长度
            for i in range(strslen-1):
                if len(strs[i]) <= len(strs[i+1]):
                    strlen = len(strs[i])
                else:
                    strlen = len(strs[i+1])
            # 按最短字符长度遍历字符串，并按位对比
            for j in range(strlen):
                for i in range(strslen - 1):
                    if strs[i][j:j+1:1] != strs[i+1][j:j+1:1]:
                        return strstr
                strstr += strs[i][j:j+1:1]

        return strstr

```
### 思路：
***
先判断字符数组长度，长度为1直接返回数组内容;长度大于1,找出数组内最短字符串的长度，按此长度遍历各个字符串，对比相应位子的元素是否相同