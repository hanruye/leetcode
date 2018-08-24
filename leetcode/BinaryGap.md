### 问题描述：
***
给定正整数N，找出其对应二进制数中相邻1距离的最大值。
### 代码实现：
***
```python
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        countlist = []
        binarystr = self.get_binary(N)
        first_index = -1
        secon_index = -1

        strl = len(binarystr)

        for i in range(strl):
            """
            if binarystr[i] == "1" and first_index == -1:
                first_index = i
            elif binarystr[i] == "1":
                secon_index = i
            """

            if binarystr[i] == "1":
                secon_index = i

            if first_index != -1 and secon_index != -1:
                countlist.append(secon_index - first_index)
                # first_index = secon_index
            first_index = secon_index

        if not countlist:
            return 0
        else:
            return max(countlist)

    # 十进制转换二进制
    def get_binary(self, nums):
        binarystr = ""
        if nums == 0:
            binarystr = "0"

        while nums:
            binarystr += str(nums % 2)
            nums = nums // 2

        return binarystr[::-1]

```
