### 问题描述：
***
给定二叉树，返回树中任意两个不同节点的值之间的最小差。
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        note_value = []
        note_value = self.get_notes_value(root, note_value)
        minnum = abs(note_value[1] - note_value[0])
        # 遍历获取最小差值
        for i in range(len(note_value)):
            for j in range(i+1, len(note_value)):
                if abs(note_value[j] - note_value[i]) < minnum:
                    minnum = abs(note_value[j] - note_value[i])
        return minnum
    # 递归获取每个节点数值
    def get_notes_value(self,root, value_list):
        if root:
            value_list.append(root.val)
            self.get_notes_value(root.left, value_list)
            self.get_notes_value(root.right, value_list)
        return value_list
```
### 总结：
***
1. 思路：第一步遍历二叉树整体，找出每个节点的数值，第二步循环计算差值并确定最小值。