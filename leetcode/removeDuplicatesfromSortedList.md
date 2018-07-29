### 问题描述：
***
给定已排序单程链表，保留非重复节点。

### 代码实现：
***
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, list1):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not list1:
            return list1
        head_list = now_list = list1
        while now_list.next != None:
        # 比较当前节点值与下一节点值，若相等当前节点指向下下节点，若不想等当前节点跳至下一节点
            if now_list.val == now_list.next.val:
                now_list.next = now_list.next.next
            else:
                now_list = now_list.next
        return head_list
```
