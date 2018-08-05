### 问题描述：
***
给定二叉树和特定数，判断是否有通道的节点数和与特定数相等
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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

```
### 总结：
***
1. 递归方法+短路或。递归逐个判断每一条通道是否满足条件，找到满足条件的通道后，根据或运算的短路功能跳出递归。