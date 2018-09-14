### 问题描述：
***
链表排序
### 代码实现：
***
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, now_note):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 当前节点为空下一节点为空
        if now_note is None or now_note.next is None:
            return now_note

        # 获取当前节点后面已排序好的子链表首节点
        next_note = self.insertionSortList(now_note.next)

        # 当前节点与子链表比较值大小并排序，返回已排序好的链表首节点
        temp_note = next_note
        # 情况1：当前节点值小于子链表首节点值
        if now_note.val <= temp_note.val:
            return now_note
            # 情况2：当前节点值大于子链表首节点值，且当前节点后只有1个节点
        elif not temp_note.next:
            # 改变指针指向
            now_note.next = None
            temp_note.next = now_note
            return temp_note
        # 情况3：当前节点值大于子链表首节点值，且当前节点后子链表个数大于1
        pointer = temp_note
        # 遍历子链表 查找链表中比当前节点值大的第-1个数
        while temp_note.next and temp_note.next.val < now_note.val:
            temp_note = temp_note.next
        # 改变指针指向
        now_note.next = temp_note.next
        temp_note.next = now_note
        return pointer
```