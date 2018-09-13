
### 问题描述：
***
给定一个字符串s和一个非空字符串p，求出s中所有p构词法的起始指标。
### 代码实现：
***
```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        sl, pl = len(s), len(p)
        if sl < pl:
            return []
        templist = []
        for i in range(sl-pl+1):
            if self.isAnagram(s[i:i+pl], p):
                templist.append(i)
        return templist
    
    # 判断t是否是s的回文构词法
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
                if dic[ele] >= 1:
                    dic[ele] -= 1
                else:
                    return False
            else:
                return False
        # 验证
        #keylist = dic.keys()
        #for ele in keylist:
            #if dic[ele] != 0:
                #return False

        return True
```
### 总结：
***
1. timeout 版本。

