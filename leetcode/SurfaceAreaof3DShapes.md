### 问题描述：
***
给定N×N网格，在每个网格上堆叠1×1×1的立方体。每个网格上的数字代表堆叠立方体个数，问3D的表面积。
### 代码实现：
***
```python
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0 # 面积
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    value = grid[i][j] * 6 - 2 * (grid[i][j] - 1)  # 每个立方体有6个面，减去且有重合面
                    # 减去正上方遮挡
                    if i > 0:
                        value -= self.get_grid_value(grid, [i-1, j], [i, j])
                    # 减去正下方遮挡
                    if i < m - 1:
                        value -= self.get_grid_value(grid, [i + 1, j], [i, j])
                    # 减去正左方遮挡
                    if j > 0:
                        value -= self.get_grid_value(grid, [i, j-1], [i, j])
                    # 减去正右方遮挡
                    if j < n - 1:
                        value -= self.get_grid_value(grid, [i, j+1], [i, j])
                    # 容错
                    if value < 0:
                        value = 0
                else:
                    value = 0
                sum += value
        return sum
    # 获取待减值
    def get_grid_value(self,grid, point1, point2):
        if grid[point1[0]][point1[1]] <= grid[point2[0]][point2[1]]:
            return grid[point1[0]][point1[1]]
        else:
            return grid[point2[0]][point2[1]]
```