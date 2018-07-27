### 问题描述：
***
给定两个二进制字符串，将两个字符串相加返回新的字符串。例如：str1 = "11",str2 = "1",返回str3 = "100"
### 代码实现：
***
```python
class Solution(object):
    def addBinary(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        summ = ""
        c_now = l = ll = v_now = c_pre = 0
        l1 = len(str1)
        l2 = len(str2)
        ll = abs(l1 - l2)
        if l1 > l2:
            summ,c_now = Solution().addBinaryThree(l2,summ,str1,str2)
            summ,c_now = Solution().addBinaryFour(l2,ll,summ,str1,c_now)
        elif l1 < l2:
            summ, c_now = Solution().addBinaryThree(l1, summ, str2, str1)
            summ, c_now = Solution().addBinaryFour(l1, ll, summ, str2, c_now)
        else:
            summ, c_now = Solution().addBinaryThree(l1, summ, str2, str1)
        
        if 0 != c_now:
            summ += str(c_now)

        return summ[::-1]

    # 1位二进制加法
    def addBinaryOne(self,v1_now, v2_now, c_pre):
        #c_now = 0
        c_now = (v1_now+c_pre+v2_now)//2
        v_now = (v1_now+c_pre+v2_now) % 2
        return c_now, v_now

    def addBinaryThree(self,ls, summ, strl, strs):
        c_now  = v_now = c_pre = 0
        for i in range(0, ls):
            c_pre = c_now
            c_now, v_now = Solution().addBinaryOne(int(strl[len(strl) - i - 1]), int(strs[len(strs) - i - 1]), c_pre)
            summ += str(v_now)

        return summ, c_now


    def addBinaryFour(self,l, ll, summ, strstr, c_now):
        for i in range(l, l+ll):
            c_pre = c_now
            c_now, v_now = Solution().addBinaryOne(int(strstr[len(strstr) - i - 1]), 0, c_pre)
            summ += str(v_now)

        return summ, c_now

              
```
### 总结：
***
1. 知识点：python面向对象，功能拆分，字符串按位取反
2. 思路：先按最短字符串二进制加法，获取进位c和反向值，再按最长字符串剩余位数与之前进位c二进制加法，获取当前进位C和反向值，最后反向输出结果。