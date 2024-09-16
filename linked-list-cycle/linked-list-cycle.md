# Linked List

+ [Linked List Cycle](#linked-list-cycle)

[comment]: <> (Stop)

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    k = False
    first = second = head
    while (second is not None and second.next is not None):
        first = first.next
        second = second.next.next
        if (first == second):
            k = True
            break
    return k
```