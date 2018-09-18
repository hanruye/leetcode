### 问题描述：
***
给定页面面积设计页面的长和宽。规则：1.要求面积不变。2.长>= 宽3.长与宽差距尽可能小
### 代码实现：
***
```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        
        if area == 0 or area == 1:return [area, area]

        temp_len = area//2
        lengthlist = []
        for i in range(1,temp_len+1):
            lenth = area/i
            if area == i * lenth:
                lengthlist.append([i,lenth])
        
        mindistance = abs(lengthlist[0][0]-lengthlist[0][1])
        lwlist = [lengthlist[0][0],lengthlist[0][1]]
        for ele in lengthlist:
            if mindistance > abs(ele[0]-ele[1]):
                mindistance = abs(ele[0]-ele[1])
                lwlist = ele
        return sorted(lwlist,reverse=True) 
        """
        if area == 0: return [area, area]
        
        temp = int(math.sqrt(area))
        while area % temp != 0:
            temp -= 1

        return [area/temp, temp]
         
```