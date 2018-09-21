### 问题描述：
***
给定字符串（字符全部为a-z之间），要求判断字符串是否可组成回文字符串，至多删除1个字符，若删除字符后字符串是回文字符也算是。
### 代码实现：
***
```python
import re
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tempstrlist = list(s)
        if not self.is_Palindrome(s):
            for i in range(len(s)):
                aa = tempstrlist.pop(i)
                #bb = "".join(tempstrlist)
                if self.is_Palindrome("".join(tempstrlist)):
                    return True
                tempstrlist.insert(i, aa)
            return False

        return True

    
    def is_Palindrome(self, s):
   
        #s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return s == s[::-1]

```