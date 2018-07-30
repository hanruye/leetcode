### 问题描述：
***
给定两个二叉树，判断是否相等
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append((q, p))
        while stack:
            q_now, p_now = stack.pop()
            # 两个对应节点为空，进行下次循环
            if not q_now and not p_now:
                continue

            # 对应节点位非空
            if q_now and p_now:
                if q_now.val != p_now.val:
                    return False
                # 将当前层对应节点下一层的左右对称节点推入堆栈
                stack.append((q_now.left, p_now.left))
                stack.append((q_now.right, p_now.right))
            else:# 结构不同
                return False

        return True

```

### 总结：
***
1. 思路：二叉树相等，既要求有相同的结构又要求对应节点的数相等。用列表模拟堆栈存储，循环入栈和出栈。初次将两个树首节点压入堆栈。步骤1.开始循环，弹出堆栈节点内容，满足相等条件后，将下层对应点推入堆栈，进入步骤1再次判断，依次类推，直至找到不同点退出或确定两树相同退出。