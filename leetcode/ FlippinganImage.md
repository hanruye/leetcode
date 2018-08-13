
### 问题描述：
***
给定二维二进制数组代表一张图片，要求图片水平镜像后再反转图片
### 代码实现：
***
```python
class Solution(object):
    def flipAndInvertImage(self, binarryone):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        binarrytwo = []
        binarrythree = []
        # 水平镜像
        for templist in binarryone:
            templistlist = templist[::-1]
            binarrytwo.append(templistlist)
        # 反转图片
        for temp in binarrytwo:
            for i in range(len(temp)):
                if temp[i] == 1:
                    temp[i] = 0
                else:
                    temp[i] = 1
            binarrythree.append(temp)
        return binarrythree

```
### 总结
***
1. 思路：图片水平镜像既是一位数组反转，图片反转既是元素0和1对转。