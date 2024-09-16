# Tree

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

[comment]: <> (Stop)

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
def kthSmallest(self, root, k):
    queue = []
    while True:
        while root:
            queue.append(root)
            root = root.left
        root = queue.pop(-1)
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```