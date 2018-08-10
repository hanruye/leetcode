
### 问题描述：
***
根据给定二维数组内元素的大小和个数，在3D空间中，使用1×1×1立方体堆积木，计算在3个平面上的投影面积。
### 代码实现：
***
```python
class Solution(object):
    def projectionArea(self, list2D):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i = len(list2D)# 行
        j = len(list2D[0])# 列

        Sxy = Sxz = Syz = 0
        for x in range(i):
            # xz轴上的投影面积为全部行向量最大元素的和
            Sxz += max(list2D[x])
            for y in range(j):
                # xy轴上的投影面积为二维数组中大于0的元素个数
                if list2D[x][y] > 0:
                    Sxy += 1

        # yz 轴上的投影面积为全部列向量最大元素的和
        for k in range(j):
            Syz += max([temp[k] for temp in list2D])# 列切片

        return Sxy + Syz + Sxz
```
### 总结：
***
1. python 二维数组列切片：[temp[k] for temp in list2D]
2. 思路：在xy轴上的投影面积为二维数组中大于0的元素个数;在xz轴上的投影面积为全部行向量最大元素的和;在yz 轴上的投影面积为全部列向量最大元素的和。