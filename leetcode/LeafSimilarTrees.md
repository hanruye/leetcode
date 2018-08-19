### 问题描述：
***
给定两个二叉树，判断树首是否相同
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
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        #listone = listtwo = [] #此时两个变量指向同一个地址，故值是一样的
        listone = []
        listtwo = []
        self.getLeafs(root1, listone)
        self.getLeafs(root2, listtwo)
        
        if len(listone) != len(listtwo):
            return False
        else:
            for i in range(len(listone)):
                if listone[i] != listtwo[i]:
                    return False
            return True
    # 计算二叉树，树顶值。
    def getLeafs(self, treeNode, tempList):

        if not treeNode.left and not treeNode.right:
            tempList.append(treeNode.val)

        if treeNode.left:
            self.getLeafs(treeNode.left, tempList)
        if treeNode.right:
            self.getLeafs(treeNode.right, tempList)
```
### 总结：
***
1. 指针指向
2. 思路：递归得出二叉树全部树叶值，循环遍历元素是否相同。
