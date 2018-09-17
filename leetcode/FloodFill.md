### 问题描述：
***
给定2维数组代表一张图片，给定初始填充像素位置及填充色值。填充规则：填充像素起始位置始，朝向4个方向填充，直至遇到与当前像素值不相同的像素停止填充。
### 代码实现：
***
```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def fill(x, y, pre_pixel):
            # 像素点坐标范围超出图片范围，退出递归
            if x < 0 or x > len(image)-1 or y < 0 or y > len(image[0])-1:return
            # 获取当前像素值
            now_pixel = image[x][y]
            # 当前像素值与前像素值不同（或填充起始位置与填充色颜色一致），退出递归
            if now_pixel != pre_pixel or now_pixel == newColor:return
            image[x][y] = newColor # 像素填充
            fill(x-1, y, now_pixel)
            fill(x, y-1, now_pixel)
            fill(x+1, y, now_pixel)
            fill(x, y+1, now_pixel)

        fill(sr, sc, image[sr][sc])
        return image

```
### 总结：
***
1. 方法体中可以定义方法体
2. 思路：按4个方向递归填充，直至图像边界停止或遇到不同像素值停止。