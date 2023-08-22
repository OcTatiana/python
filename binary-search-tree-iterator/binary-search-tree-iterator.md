# Tree

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)

[comment]: <> (Stop)

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
def __init__(self, root):
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left
def next(self):
    res = self.stack.pop()
    root = res
    root = root.right
    if root:
        while root:
            self.stack.append(root)
            root = root.left
    return res.val
def hasNext(self):
    return self.stack != []
```