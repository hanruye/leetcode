### 问题描述：
***
给定二叉树，判断是否深度平衡。深度平衡定义：一个二叉树，每个节点的两个子树的深度不超过1。
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        #print(self.isBalancedHelper(root))
        if not self.isBalancedHelper(root):return False
        return True
    # 判断当前节点是否平衡
    def isBalancedHelper(self, root):
        if not root:return 0

        L_deep = self.isBalancedHelper(root.left)
        #print L_deep
        R_deep = self.isBalancedHelper(root.right)
        #print R_deep
        # 当前节点左支或右支下的节点已非平衡
        if L_deep is None or R_deep is None:
            return None

        # 若当前节点的左支右支深度大于1
        if abs(L_deep-R_deep)>1:
            return None

        return max([L_deep, R_deep]) + 1

```
### 总结：
***
1. 思路：递归判断每个节点的左右支是否平衡。