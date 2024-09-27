# Math

+ [Fibonacci Number](#fibonacci-number)

[comment]: <> (Stop)

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
    a, b, c = 0, 1, 0
    i = 0
    if N < 2:
        return N
    for i in range(N-1):
        c = a + b
        a = b
        b = c
        c = 0
    return b
```