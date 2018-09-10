### 问题描述：
***
给定一个任意的赎金通知字符串和另一个包含所有杂志信件的字符串，如果可以从杂志构造出赎金通知，则编写一个返回true的函数;否则，它将返回false。
杂志弦上的每一个字母只能在你的勒索信中使用一次。
### 代码实现：
***
```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        templist = [element for element in magazine]
        for i in range(len(ransomNote)):
            if ransomNote[i] not in templist:
                return False
            else:
                templist.remove(ransomNote[i])
        return True

```
### 总结：
***
1. 思路：如果杂志字符串少于赎金字符串，必定无法完成赎金书写;遍历赎金字符串中的每个字符，判断是否在杂志字符串中。