# Linked List

+ [Sort List](#sort-list)

[comment]: <> (Stop)

## Sort List

https://leetcode.com/problems/sort-list/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    head = l3
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            l3.next = l1
            l1 = l1.next
        else:
            l3.next = l2
            l2 = l2.next
        l3 = l3.next
    if l1 is None:
        l3.next = l2
    if l2 is None:
        l3.next = l1
    return head.next
def sortList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    tmp = None
    while fast and fast.next:
        tmp = slow
        slow = slow.next
        fast = fast.next.next
    tmp.next = None
    return self.mergeTwoLists(self.sortList(head), self.sortList(slow))
```