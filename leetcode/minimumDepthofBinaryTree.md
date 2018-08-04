### 问题描述：
***
给定二叉树，计算树顶至无子节点的节点的距离
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        floor = 0
        stack = []
        stack.append(tuple([root]))
        while stack:
            floor += 1
            temp_tuple = stack.pop()
            temp_list = []
            for i in range(len(temp_tuple)):
                if not temp_tuple[i].left and not temp_tuple[i].right:
                    return floor
                else:
                    if temp_tuple[i].left:
                        temp_list.append(temp_tuple[i].left)
                    if temp_tuple[i].right:
                        temp_list.append(temp_tuple[i].right)

            if len(temp_list) > 0:
                stack.append(tuple(temp_list))


```
### 总结：
***
1. 思路：找无子节点的节点所在树层即可