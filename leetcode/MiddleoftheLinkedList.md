### 问题描述：
***
给定单链表，返回中间节点，若节点个数为偶数个，返回中间两个节点的第二个节点
### 代码实现：
***
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, listnode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        templist = listnode
        while templist:
            i += 1
            templist = templist.next
        # 找到中间节点的位置
        i = i // 2 + 1

        templist = listnode
        j = 0
        while templist:
            j += 1
            if j == i:
                return templist

            templist = templist.next
```
### 总结：
***
1. 思路：第一次遍历全部节点找到中间节点的位置，第二次遍历节点找出需要返回的节点