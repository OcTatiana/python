# Math

+ [Sqrt(x)](#sqrtx)

[comment]: <> (Stop)

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> int:
    res = 0
    while res**2 <= x:
        res = res + 1
    return res - 1
```