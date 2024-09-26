# Tree

+ [Validate Binary Search Tree](#validate-binary-search-tree)

[comment]: <> (Stop)

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
def isValidBST(self, root):
    def helper(node, lower, upper):
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        return True
    return helper(root, -2**31 - 1, 2**31)
```