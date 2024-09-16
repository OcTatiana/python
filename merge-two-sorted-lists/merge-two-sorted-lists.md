# Linked List

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

[comment]: <> (Stop)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = head = ListNode()
    while l1 is not None and l2 is not None:
        if (l1.val <= l2.val):
            l3.next = ListNode(l1.val, None)
            l1 = l1.next
        else:
            l3.next = ListNode(l2.val, None)
            l2 = l2.next
        l3 = l3.next
    if l1 is None:
        while l2 is not None:
            l3.next = ListNode(l2.val, None)
            l3 = l3.next
            l2 = l2.next
    else:
        while l1 is not None:
            l3.next = ListNode(l1.val, None)
            l3 = l3.next
            l1 = l1.next
    return head.next
```