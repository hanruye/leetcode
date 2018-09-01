### 问题描述：
***
左右反转二叉树。
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        flags = True
        stack = []
        next_stack = []
        stack.append(root)
        while flags:
            while stack:
                node = stack.pop()
                temp_left = None
                temp_right = None
                if node.left:
                    temp_left = node.left
                if node.right:
                    temp_right = node.right
                node.left = temp_right
                node.right = temp_left
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            stack = next_stack
            if not stack:
                flags = False
        return root
```
### 总结：
***
1. 思路：交换每个节点的下一层节点的位置即可。