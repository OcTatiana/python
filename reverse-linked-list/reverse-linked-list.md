# Linked List

+ [Reverse Linked List](#reverse-linked-list)

[comment]: <> (Stop)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
    cur = None
    while head is not None:
        tmp = head.next
        head.next = cur
        cur = head
        head = tmp
    return cur
```