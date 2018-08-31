### 问题描述：
***
给定单词组成的字符串，每个单词仅由大小写字母组成。如果单词的首个字符是元音(a,e,i,o,u)，则在单词后加上“ma”字符串，再根据单词的位置index追加index个“a”字符;如果单词首个字符不为元音，则将首个字符移动至单词末尾，再执行上面操作。
### 代码实现：
***
```python
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        elelist = ["a", "e", "i", "o", "u"]
        wordslist = S.split(" ")
        sentencelist = []
        sentence = ""
        for i in range(len(wordslist)):
            if self.get_low_alp(wordslist[i][:1]) in elelist:
                sentencelist.append(wordslist[i]+self.get_str(i))
            else:
                sentencelist.append(wordslist[i][1:] + wordslist[i][:1] +self.get_str(i))

        for ele in sentencelist:
            sentence += ele + " "
        return sentence[:len(sentence)-1]
    # 获取尾部添加字符串
    def get_str(self,num):
        tempstr = "ma"
        for i in range(num+1):
            tempstr += "a"
        return tempstr
    # 大写字母转小写
    def get_low_alp(self,c):
        if ord(c) in range(ord("A"), ord("Z")+1):
            return chr(ord(c)+32)
        return c

```