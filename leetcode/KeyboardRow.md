### 问题描述：
***
给定单词列表，找出在列表中在同一行的单词
### 代码实现：
***
```python
class Solution(object):
    def findWords(self, originalList):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstrow = "qwertyuiop"
        secondrow = "asdfghjkl"
        thirdrow = "zxcvbnm"
        templist = []
        for element in originalList:
            if self.isinstr(element, firstrow, templist) or \
               self.isinstr(element, secondrow, templist) or \
               self.isinstr(element, thirdrow, templist):
                pass
        return templist
    # 判断单词是否在同一行
    def isinstr(self, element, rowstr, templist):
        ele = element.lower()
        flag = True
        if ele[:1] in rowstr:
            for i in range(1, len(ele)):
                if ele[i] not in rowstr:
                    flag = False
                    break
        else:
            flag = False
        if flag:
            templist.append(element)
        return flag
```
### 总结：
***
1. 思路：先找出每个单词首字母所在行，判断单词其他字母是否在当前行。
