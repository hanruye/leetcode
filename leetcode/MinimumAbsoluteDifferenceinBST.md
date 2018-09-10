### 问题描述：
***
给定一个具有非负值的二叉树，求任意两个节点值之间的最小绝对差。
### 代码实现：
***
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        array, temp_array = [], []
        self.travel_all_notes(root, array)
        array = sorted(array)
        for i in range(1, len(array)):
            temp_array.append(array[i] - array[i - 1])
        temp_array = sorted(temp_array)
        return temp_array[0]
    
    def travel_all_notes(self,root,array):
        array.append(root.val)
        if root.left:
            self.travel_all_notes(root.left, array)
        if root.right:
            self.travel_all_notes(root.right, array)
```
### 总结：
***
1. 思路：首先遍历每个节点生成节点值列表;将列表升序（小技巧，目的是减少查询最小绝对值差的循环次数），升序后每两位求差，最后找出最小差值。