# Linked List

+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

[comment]: <> (Stop)

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    l = 0
    h1, h2 = head, head
    while (h1 is not None):
        h1 = h1.next
        l = l + 1
    if (l > n):
        l = l - n - 1
        while (l > 0):
            h2 = h2.next
            l = l - 1
        if (h2.next is not None):
            h2.next = h2.next.next
        else:
            head = None
    else:
        head = head.next
    return head
```