### 问题描述：
***
给定n个非负整数a1 a2…， an，其中每一个都表示坐标(i, ai)上的一个点。画了n条垂直线，使直线i的两个端点在(i, ai)和(i, 0)处，找出两条直线，与x轴一起形成一个容器，使容器中含有最多的水。
## 示例图
![result4](assets/ContainerWithMostWater.jpg)
### 代码实现：
***
```python
class Solution(object):
    def maxArea(self, height):
        """
        l = len(height)

        area = []
        for i in range(l-1):
            temp = []
            for j in range(i+1, l):
                temp.append(min(height[i], height[j])*(abs(j-i)))
            if temp: area.append(temp)
        area.append([])
        for l in range(len(area[0])):
            area[-1].append(max(area[l]))
        return max(area[-1])
        
        """
        l = len(height)
        be = 0 # 前面的index
        af = l-1 # 后面的index
        area = af*min(height[af], height[be])
        while be < af:
            if height[be] < height[af]:
                be += 1
            else:
                af -= 1
            area = max(area, (af-be)*min(height[af], height[be]))
        return area
```