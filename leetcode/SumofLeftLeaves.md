### 问题描述：
***
给定二叉树，返回所有左末支和。
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        summ = 0
        # 递归退出条件1, 2
        if not root: return summ # 1 
        if not root.left and not root.right: return summ # 2 
        if root.left and not root.left.left and not root.left.right: summ = root.left.val # 判断左末支
        return summ + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) # 返回当前节点的左末支与
```
### 总结：
***
1. 思路：递归法。