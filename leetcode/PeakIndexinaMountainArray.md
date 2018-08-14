
### 问题描述：
***
给定山峰形式的数组，返回山顶所在数组的下标。
### 代码实现：
***
```python
class Solution(object):
    def peakIndexInMountainArray(self, arraylist):
        """
        :type A: List[int]
        :rtype: int
        """
        index_L = index_R = 0
        l = len(arraylist)
        if l == 0:
            return 0
        #以10个分组
        count = l // 10
        if count <= 1:
            for i in range(l-1):
                if arraylist[i] > arraylist[i+1]:
                    return i
        else:
            # 锁定山峰范围
            for j in range(0, count+1):
                if arraylist[j*10] > arraylist[j*10+1]:
                    index_L = (j - 1) * 10
                    index_R = j * 10
                    break
            # 若山峰居右
            if index_L == 0 and index_R == 0:
                index_L = count * 10
                index_R = l
            # 在已锁定的山峰范围内，遍历比较最大值
            for k in range(index_L, index_R+1):
                if arraylist[k] > arraylist[k+1]:
                    return k
```
### 总结：
***
1. 思路：获取数组长度，若长度小于等于10,直接遍历比较大小。若长度大于10,将数组以10个元素为1组分组，若第i个分组的首个元素大于第2个元素，则峰值在前一组中即第i-1组，若前面整10元素组中不存在峰值，则峰值在剩余元素中。