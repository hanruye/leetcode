
### 问题描述：
***
给定二叉树，计算其深度
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
    def maxDepth(self, b):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = 0
        stack = []
        if not b:
            return num

        stack.append(tuple([b]))
        num += 1
        while stack:
            temp_tuple = stack.pop()
            temp_len = len(temp_tuple)
            temp_num = 0
            temp_list = []

            for i in range(temp_len):
                if temp_tuple[i].left:
                    if temp_num == 0:
                        temp_num = 1
                    temp_list.append(temp_tuple[i].left)
                if temp_tuple[i].right:
                    if temp_num == 0:
                        temp_num = 1
                    temp_list.append(temp_tuple[i].right)

            if len(temp_list) > 0:
                temp_list = tuple(temp_list)
                stack.append(temp_list)
            num += temp_num

        return num

        
```
### 总结：
***
1. 思路：首先判断一层是否存在节点，若有节点存在，将该层所有存在节点归组，再依次判断每一个节点的下一层节点是否存在，继续分组。依次类推，直至下一层不存在任何一个节点。