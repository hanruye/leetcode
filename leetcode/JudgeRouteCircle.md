### 问题描述：
***
机器人位于位置(0,0)，给定字符串(由U，D，L，R，U代表向上移动1位，D代表向下移动1位，L代表向左移动1位，R代表向右移动1位)组成，判断机器人按字符串移动后，是否回到原位置。
### 代码实现：
***
```python
class Solution(object):
    def judgeCircle(self, strnum):
        """
        :type moves: str
        :rtype: bool
        """
        dic = {"U": 1, "D": -1, "L": 1, "R": -1}
        position = [[0], [0]]
        while strnum:
            if strnum[0] == "U":
                position[0][0] += dic["U"]
                strnum = strnum[1:len(strnum)]
            elif strnum[0] == "D":
                position[0][0] += dic["D"]
                strnum = strnum[1:len(strnum)]
            elif strnum[0] == "L":
                position[1][0] += dic["L"]
                strnum = strnum[1:len(strnum)]
            elif strnum[0] == "R":
                position[1][0] += dic["R"]
                strnum = strnum[1:len(strnum)]
        if position[0][0] == 0 and position[1][0] == 0:
            return True
        return False

```
### 总结：
***
1. 思路：以二维数组记录机器人当前位置，第一位记录上下移动，第二位记录左右移动。将UDLR按字典存储，每次截取字符串的首位，判断其移动方式。