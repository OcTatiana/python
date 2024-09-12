# Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)

[comment]: <> (Stop)

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
    arr = []
    l = 0
    while head is not None:
        arr.append(head)
        head = head.next
        l = l + 1
    return arr[l//2]
```