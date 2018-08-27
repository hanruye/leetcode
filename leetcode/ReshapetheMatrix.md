### 问题描述：
***
根据需要重新确定向量的维数。实现numpy.reshape(r,c)方法。
### 代码实现：
***
```python
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m*n != r*c:
            return nums

        # 将原始向量转换成1xn 中间向量
        templist = []
        for i in range(m):
            for j in range(n):
                templist.append(nums[i][j])

        # print (templist)
        # 将中间向量转成rxn向量
        newnums = []
        count = 0
        for p in range(r):
            temp = []
            for q in range(c):
                temp.append(templist[count])
                count += 1
            newnums.append(temp)

        # print (newnums)
        return newnums

```
### 总结：
***
1. 思路：reshape前后元素个数及大小不变。将原始向量（m,n）reshape成中间临时向量(1,mxn),继而从中间临时向量reshape成（r,c）向量。
