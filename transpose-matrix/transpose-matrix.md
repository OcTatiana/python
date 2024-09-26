# Array

+ [Transpose Matrix](#transpose-matrix)

[comment]: <> (Stop)

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    res = []
    for i in range(len(A[0])):
        tmp = []
        for j in range(len(A)):
            tmp.append(A[j][i])
        res.append(tmp)
    return res
```