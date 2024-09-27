# Linked List

+ [Linked List Cycle II](#linked-list-cycle-ii)

[comment]: <> (Stop)

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
    k = False
    first = second = head
    while (second is not None and second.next is not None):
        first = first.next
        second = second.next.next
        if (first == second):
            k = True
            break
    if k is False:
        return None
    second = head
    while (first != second):
        first = first.next
        second = second.next
    return first
```