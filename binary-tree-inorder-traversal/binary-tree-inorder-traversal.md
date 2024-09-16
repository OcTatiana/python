# Tree

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

[comment]: <> (Stop)

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
def inorderTraversal(self, root):
    res = []
    self.traverse(root, res)
    return res
def traverse(self, node, res):
    if node is None:
        return
    self.traverse(node.left, res)
    res.append(node.val)
    self.traverse(node.right, res)
```