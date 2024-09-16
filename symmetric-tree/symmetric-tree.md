# Tree

+ [Symmetric Tree](#symmetric-tree)

[comment]: <> (Stop)

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
def invertTree(self, root):
    if root is None:
        return None
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    return root
def symmetric(self, l, r):
    if l is None and r is None:
        return True
    if l is None or r is None:
        return False
    return ((r.val == l.val) and self.symmetric(l.left, r.left) and self.symmetric(l.right, r.right))
def isSymmetric(self, root):
    if root is None:
        return True
    return self.symmetric(root.left, self.invertTree(root.right))
```