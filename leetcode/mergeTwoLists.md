### 问题描述：
***
给定两个已从小到大排序的链表，合并成一个同样顺序的链表
### 代码实现：
***
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = now = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                now.next = l1# 当前节点指向l1节点
                l1 = l1.next # l1跳至l1下一节点
            else:
                now.next = l2
                l2 = l2.next
            now = now.next #当前节点跳至当前节点指向的节点（原l1节点或l2节点）
        now.next = l1 or l2
        pre = pre.next # 删除初始节点
        return pre
                
```
### 总结：
***
1. 链表知识：一种数据存储结构，内存地址不一定相邻，当前节点存有指向下一个节点的地址，便于修改不便于查询。
