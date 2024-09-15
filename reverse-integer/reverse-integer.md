# Math

+ [Reverse Integer](#reverse-integer)

[comment]: <> (Stop)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
    if x >= 0:
        a = (str)(x)[::-1]
        x = (int)(a)
    else:
        a = (str)(-x)[::-1]
        x = -(int)(a)
    if x < -2**31 or x > 2**31 - 1:
        return 0
    return x
```