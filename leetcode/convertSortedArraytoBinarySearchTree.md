### 问题描述：
***
给定升序数组，生成高度对称二叉树
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
    def sortedArrayToBST(self, temp_notelist):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not temp_notelist:
            return None
    
        # 数组重排
        notelist=[]
        L = len(temp_notelist)
        if L == 1:
            notelist = temp_notelist
        else:
            # 找到中间点位置
            middle_index = len(temp_notelist)//2
            notelist.append(temp_notelist[middle_index])

            temp_notelist_left = temp_notelist[0:middle_index]
            temp_notelist_right = temp_notelist[middle_index+1:L]
            while temp_notelist_right or temp_notelist_left:
                if temp_notelist_left:
                    notelist.append(temp_notelist_left.pop())
                if temp_notelist_right:
                    notelist.append(temp_notelist_right.pop())
        notelist = notelist[::-1]

        stack = []# 存放上层节点信息
        i = 0 # 记录当前第几层
        treetop = TreeNode(notelist.pop())
        stack.append(tuple([treetop]))

        while stack:
            i += 1 # 跳转至下一层
            temp_tuple = stack.pop()# 获取上一层节点信息
            last_note_num = len(temp_tuple)
            remain_note_num = len(notelist) # 剩余节点个数
            temp_list = [] # 存放当前层节点信息
            if remain_note_num >= 2**i:#  剩余节点个数大于当前层满点个数
                # 建立链接
                for l in range(last_note_num):
                    temp_tuple[l].left = TreeNode(notelist.pop())
                    temp_tuple[l].right = TreeNode(notelist.pop())
                    temp_list.append(temp_tuple[l].left)
                    temp_list.append(temp_tuple[l].right)
            elif remain_note_num >= 2**(i-1):
                for l in range(last_note_num):
                    temp_tuple[l].left = TreeNode(notelist.pop())
                    temp_list.append(temp_tuple[l].left)
                for l in range(len(notelist)):
                    temp_tuple[l].right = TreeNode(notelist.pop())
                    temp_list.append(temp_tuple[l].right)
            elif remain_note_num > 0:
                for l in range(len(notelist)):
                    temp_tuple[l].left = TreeNode(notelist.pop())
                    temp_list.append(temp_tuple[l].left)
            if len(temp_list) > 0:
                stack.append(tuple(temp_list))
        return treetop
    # 这题有毒

```
### 总结：
***
1. 思路：首先数组重排，其次按照高度对称生成二叉树