### 问题描述：
***
给定两个字符串A，B，单词以空格分开，返回不重复单词列表（例：某单词在A中不重复，且不存在B中）
### 代码实现：
***
```python
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        teplist = []  # 存储单个元素
        dic = {}  # 存储每个元素出现的次数

        alist = A.split()
        blist = B.split()

        for element1 in alist:
            if element1 not in dic:
                dic[element1] = 1
            else:
                dic[element1] += 1

        for element in blist:
            if element not in dic:
                dic[element] = 1
            else:
                dic[element] += 1

        for ele in dic:
            if dic[ele] == 1:
                teplist.append(ele)
        
        return teplist
```
### 总结：
***
1. 思路：使用字典键值唯一性质，统计每个单词出现的次数，最后统计出现次数为1的单词。