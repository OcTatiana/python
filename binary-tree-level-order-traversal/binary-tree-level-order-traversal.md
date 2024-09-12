# Tree

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

[comment]: <> (Stop)

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
def levelOrder(self, root):
    if root is None:
        return []
    queue = [root]
    res = [[root.val]]
    while queue:
        size = len(queue)
        l = []
        while size > 0:
            v = queue.pop(0)
            size -= 1
            if v.left is not None:
                queue.append(v.left)
                l += [v.left.val]
            if v.right is not None:
                queue.append(v.right)
                l += [v.right.val]
        if l != []:
            res.append(l)
    return res
```