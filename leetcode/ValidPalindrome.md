### 问题描述：
***
给定字符串（包含非数字字母的其他显示字符），要求判断字符串中所有字符是否可组成回文字符串。
### 代码实现：
***
```python
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        temp_str = ""
        for ele in s:
            if ord("a") <= ord(ele) and ord(ele) <= ord("z") or ord("0") <= ord(ele) and ord(ele) <= ord("9"):
                temp_str += ele

            if ord("A") <= ord(ele) and ord(ele) <= ord("Z"):
                temp_str += ele.lower()

        return temp_str == temp_str[::-1]
        """
        # 使用正则表达式保留字符串中数字、大小写字母
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]
        
        
```
### 总结：
***
1. 正则表达式
2. 思路：遍历字符串去除非数字字母等非显示字符，反转剩余字符串，判断是否是回文字符串。