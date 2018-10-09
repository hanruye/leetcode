### 问题描述：
***
给定一个只包含小写字母的排序字符列表，并给定一个目标字母，找到列表中大于给定目标的最小元素。
例如，如果目标是 'z'，字母列表是['a'， 'b']，那么答案是'a'。
### python实现：
***
```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        target_num, distance, index =ord(target), 99, 0 # 目标字符转数字，两个字符间的距离，满足条件的字符下标
        for i in range(0, len(letters)):
            temp_dis = ord(letters[i]) - target_num
            if temp_dis == ord("a") - ord("z"): temp_dis = 1
            if temp_dis > 0 and temp_dis < distance:
                distance = temp_dis
                index = i

        return letters[index]

```