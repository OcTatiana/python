# Linked List

+ [Merge k Sorted Lists](#merge-k-sorted-lists)

[comment]: <> (Stop)

## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
def mergeTwoLists(self, l1, l2):
    l3 = head = ListNode()
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
def mergeKLists(self, lists):
    if len(lists) == 0:
        return None
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 2:
        l1 = lists[0]
        l2 = lists[1]
    else:
        middle = len(lists)//2
        l1 = self.mergeKLists(lists[:middle])
        l2 = self.mergeKLists(lists[middle:])
    return self.mergeTwoLists(l1, l2)
```