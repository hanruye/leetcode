### 问题描述：
***
给定二叉树，判断是否是镜像对称。
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
    def isSymmetric(self, q):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if not q:
            return True
        elif q.left and q.right and q.left.val == q.right.val:
            stack.append((q.left, q.right))
        elif not q.left and not q.right:
            return True
        else:
            return False

        while stack:
            left, right = stack.pop()
            if left and right and left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            elif not left and not right:
                continue
            else:
                return False
        return True

```
### 总结：
***
1. 思路：由外层逐渐向内层判断是否是镜像值
