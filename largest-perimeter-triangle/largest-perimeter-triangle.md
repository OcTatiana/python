# Math

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

[comment]: <> (Stop)

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort()
    i = len(A)
    while i > 2:
        if A[i - 2] + A[i - 3] <= A[i - 1]:
            i = i - 1
        else:
            return A[i-1] + A[i-2] + A[i-3]
    return 0
```