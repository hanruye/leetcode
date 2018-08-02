### 问题描述：
***
给定二叉树，用列表倒转显示整棵树
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
    def levelOrderBottom(self, p):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        all_element_list = []
        if not p:
            return all_element_list
        stack.append(tuple([p]))

        while stack:
            temp_tuple = stack.pop()
            temp_list = []
            temp_list_tuple = []
            for element in temp_tuple:
                temp_list.append(element.val)
                if element.left:
                    temp_list_tuple.append(element.left)
                if element.right:
                    temp_list_tuple.append(element.right)
            if len(temp_list_tuple) > 0:
                stack.append(tuple(temp_list_tuple))
            all_element_list.append(temp_list)

        return all_element_list[::-1]

```

### 思路：
***
1. 从树顶向下存储每一层节点数据，最后反向输出