### 问题描述：
***
给定一个非空字符串，检查是否可以通过获取它的子字符串并将子字符串的多个副本附加到一起来构造它。您可以假设给定的字符串仅由小写英文字母组成，其长度不会超过10000。
### 代码实现：
***
```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        # 获取可以整数阶段字符串的位置列表
        substrindex = [i for i in range(1, len(s)) if len(s) % i == 0]
        # 根据每个截断子字符串，判断原字符串是否由子字符串组成
        temp_list = [s[0:ele]*(l//ele) == s for ele in substrindex]
        for ele in temp_list:
            if ele:return True
        return False   
        
```