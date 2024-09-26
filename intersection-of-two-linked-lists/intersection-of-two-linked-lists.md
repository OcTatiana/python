# Linked List

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

[comment]: <> (Stop)

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    lenA, lenB = 0, 0
    A, B = headA, headB
    while (A is not None):
        A = A.next
        lenA = lenA + 1
    while (B is not None):
        B = B.next
        lenB = lenB + 1
    if (lenA < lenB):
        while (lenA != lenB):
            headB = headB.next
            lenB = lenB - 1
    if (lenB < lenA):
        while (lenA != lenB):
            headA = headA.next
            lenA = lenA - 1
    while (headA is not None or headB is not None):
        if (headA == headB):
            return headA
        else:
            headA = headA.next
            headB = headB.next
```