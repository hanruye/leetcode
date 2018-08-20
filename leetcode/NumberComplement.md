### 问题描述：
***
给定十进制正整数，返回其补码
### 代码实现：
***
```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 十进制转二进制
        binarystr = self.get_ten_or_two(True, num)
        if not binarystr:
            binarystr = str(0)

        # 0和1转换
        temstr = ""
        for i in range(len(binarystr)):
            if binarystr[i] == "1":
                temstr += "0"
            else:
                temstr += "1"

        # 二进制转十进制
        return self.get_ten_or_two(False, temstr)

    
    def get_ten_or_two(self, flag, nums):
        # 十进制转二进制
        if flag:
            binarystr = ""
            while nums:
                binarystr += str(nums % 2)
                nums = nums // 2
            return binarystr[::-1]
        else:# 二进制转十进制
            sums = 0
            while nums:
                sums = 2 * sums + int(nums[0:1])
                nums = nums[1:]
            return sums

        
```
### 总结：
***
1. 字符串指针指向字符串常量
2. 思路：1.将十进制转换成二进制，2.二进制形式逐位取反，3.取反后的二进制转十进制