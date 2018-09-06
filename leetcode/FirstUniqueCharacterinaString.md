### 问题描述：
***
给定字符串，找出第一个元素，要求字符串中此元素的个数唯一。
### 代码实现：
***
```python  
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {} #以（元素值：个数）的形式存放元素内容
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        temp = [] # 存放个数为1的元素位置
        for ele in dic.keys():
            if dic[ele] == 1:
                for i in range(len(s)):
                    if ele == s[i]:
                        temp.append(i)
                        break
        if temp:
            return min(temp)
        return -1
          
```
### 总结：
***
1. 字典键值无序
2. 思路：以字典形式存放元素及元素在字符串中出现的个数。找出出现1此的元素，遍历找出这些元素在字符串中出现的位置，找到最靠前的位置。