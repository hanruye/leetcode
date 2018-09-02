### 问题描述：
***
给定平面上的点的列表。返回由任意3个点组成的最大三角形的面积。
### 代码实现：
***
```python
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        templist = []  # 存放所有三角形的面积
        for i in range(len(points)-2):  # 控制第1个点
            for j in range(i+1, len(points)-1):  # 控制第2个点
                for k in range(j+1, len(points)):  # 控制第3个点
                    flag, area = self.get_triangle_area(points[i], points[j], points[k])
                    if flag:
                        templist.append(area)

        return max(templist)


    # 获取三角形的面积
    def get_triangle_area(self,one, two, three):
        flag = True
        a = self.get_length(one, two)
        b = self.get_length(two, three)
        c = self.get_length(three, one)
        if self.is_triangle([a, b, c]):
            p = (a+b+c)/2
            return flag, (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            flag = False
            return flag, 0

    # 获取两点的距离
    def get_length(self,point_one,point_two):
        return((point_one[0] - point_two[0])**2 + (point_one[1] - point_two[1])**2)**0.5
    # 判断是否是三角形
    def is_triangle(self,rowlist):
        if rowlist[0] + rowlist[1] <= rowlist[2]:
            return False
        if abs(rowlist[0] - rowlist[1]) >= rowlist[2]:
            return False
        if rowlist[2] + rowlist[1] <= rowlist[0]:
            return False
        if abs(rowlist[2] - rowlist[1]) >= rowlist[0]:
            return False
        if rowlist[0] + rowlist[2] <= rowlist[1]:
            return False
        if abs(rowlist[0] - rowlist[2]) >= rowlist[1]:
            return False
        return True

```