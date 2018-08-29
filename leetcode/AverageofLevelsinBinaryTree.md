### 问题描述：
给定二叉树，计算其每一层节点值的平均值。
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        ave_num = []# 存放每一层的平均值
        node_level = []# 存放每一层的节点
        node_next_level = []# 存放下一层节点  
        flags = True
        ave_num.append(root.val)
        node_level.append(root)
        while flags:
            summ = 0.0  # 存放每一层所有节点值和
            count = 0.0  # 记录一层所有节点个数
            # 遍历下一层节点
            while node_level:
                temp_node = node_level.pop()
                if temp_node.left:
                    count += 1
                    summ += temp_node.left.val
                    node_next_level.append(temp_node.left)
                if temp_node.right:
                    count += 1
                    summ += temp_node.right.val
                    node_next_level.append(temp_node.right)
            if count != 0:
                ave_num.append(summ / count)
                node_level = node_next_level
            else:
                node_level = []
            node_next_level = []
            if not node_level:#下一层节点全部为空。
                flags = False
        return ave_num
```