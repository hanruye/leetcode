### 问题描述：
***
给定一个字符串S，将每个字母分别转换为小写或大写来创建另一个字符串。返回所有可能创建的字符串的列表。
### 代码实现：
***
```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        count_alp = 0  # 记录字符串中字母的个数
        for i in range(len(S)):
            if 1 != self.is_alp(S[i]):
                count_alp += 1
        templist = []
        for i in range(len(S)):
            if 1 == self.is_alp(S[i]):
                if not templist:
                    templist.append(S[i])
                else:
                    for n in range(len(templist)):
                        templist[n] += S[i]
            elif 2 == self.is_alp(S[i]) or 3 == self.is_alp(S[i]):
                if not templist:
                    templist.append(S[i])
                    templist.append(self.change_alp_type(S[i]))
                else:
                    bl = len(templist)
                    for j in range(bl):  # 复制
                        templist.append(templist[j])
                    for k in range(bl):  # 在每个元素后面追加字符
                        templist[k] += S[i]
                    for m in range(bl, len(templist)):
                        templist[m] += self.change_alp_type(S[i])
        #print templist
        
        if not templist:
            templist.append("")
        if len(templist) != 2**count_alp:
            print "something is going wrong ,please check your code."
            return "something is going wrong ,please check your code."
        return templist
    
    # 判断 字符是何种类型
    def is_alp(self,charx):

        if ord(charx) >= 48 and ord(charx) <= 57:  # 数字
            return 1
        if ord(charx) >= 97 and ord(charx) <= 122:  # 小写字母
            return 2
        if ord(charx) >= 65 and ord(charx) <= 90:  # 大写字母
            return 3
    
    # 大小写字母转换
    def change_alp_type(self,chary):
        if ord(chary) >= 97 and ord(chary) <= 122:  # 小写字母
            return chr(ord(chary) - 32)
        if ord(chary) >= 65 and ord(chary) <= 90:  # 大写字母
            return chr(ord(chary) + 32)


```
### 总结：
***
1. 思路：每个字母有大小写两种形式，故若字符串中有N个字母，则最后结果有2^N个结果。定义列表templist存储每个可能结果。遍历字符串S中的每个元素，若为数字，则将此数字追加在templist中每个元素末尾，若为字母，则将templist中的元素翻倍，将此字母追加在templist中前半部分每个元素的末尾，再改变此字母的大小，继续追加在templist中后半段每个元素的末尾。