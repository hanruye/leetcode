### 问题描述：
***
给定正整数，判断其二进制字符串中任意相邻两位是否相等，任意不等返回True反之返回False.
### 代码实现：
***

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tempbinary = self.get_binary(n)
        for i in range(len(tempbinary)-1):
            if tempbinary[i] == tempbinary[i+1]:
                return False
        return True

    def get_binary(self, nums):
        # 十进制转二进制
        binarystr = ""
        if nums == 0:
            binarystr = "0"

        while nums:
            binarystr += str(nums % 2)
            nums = nums // 2

        return binarystr[::-1]

```