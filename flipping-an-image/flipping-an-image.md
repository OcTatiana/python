# Array

+ [Flipping an Image](#flipping-an-image)

[comment]: <> (Stop)

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def actions(self, A: List[int]):
    A = A[::-1]
    for i, el in enumerate(A):
        A[i] = (el + 1) % 2
    return A
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    res = []
    for el in A:
        res.append(self.actions(el))
    return res
```