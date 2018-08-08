### 问题描述：
***
给定整数数组，数组中每个位置的元素代表当天股票价格，只允许买卖一次，问如何获取最大利益。
### 代码实现
***
```python
class Solution(object):
    def maxProfit(self, pricelist):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        index = 0
        for i in range(1, len(pricelist)):
            if pricelist[i] - pricelist[index] > maxp:
                maxp = pricelist[i] - pricelist[index]
            if pricelist[i] - pricelist[index] < 0:
                index = i
        return maxp
```
### 总结
***
1. 双重for循环不适用
2. 思路：首先选定数组第0位为基准位，遍历数组与之比较大小.若差值大于利益值maxp，则maxp = 差值;若差值小于0（即基准位后面的数比基准位小），则将此位置作为新的基准位（index = i）.
