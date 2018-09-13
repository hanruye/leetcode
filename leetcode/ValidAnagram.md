### 问题描述：
***
给定两个字符串s和t，写一个函数来确定t是否是s的回文构词法。
回文构词法有一个特点：单词里的字母的种类和数目没有改变，只是改变了字母的排列顺序。
### 代码实现：
***
```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 长度不同一定不满足回文构词法
        if len(s) != len(t):
            return False
        dic = {}
        # 将字符串S中的字符拆分存入字典，使用字典的键值唯一特性
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        # 遍历字符串t字符
        for ele in t:
            if ele in dic.keys():
                dic[ele] -= 1
            else:
                return False
        # 验证
        keylist = dic.keys()
        for ele in keylist:
            if dic[ele] != 0:
                return False
        
        return True
```