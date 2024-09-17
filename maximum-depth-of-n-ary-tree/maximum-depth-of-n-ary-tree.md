# Graph

+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

[comment]: <> (Stop)

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
def maxDepth(self, root: 'Node') -> int:
    if root is None:
        return 0
    else:
        depth = 0
        for i in root.children:
            depth = max(depth, self.maxDepth(i))
        return 1+depth
```