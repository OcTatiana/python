# Math

+ [Base 7](#base-7)

[comment]: <> (Stop)

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
    res = ""
    if num == 0:
        return "0"
    if num < 0:
        res = res + "-"
        num = -num
    i = 0
    while 7**i <= num:
        i = i + 1
    i = i - 1
    while num > 0:
        k = 0
        while k * (7**i) <= num:
            k = k + 1
        k = k - 1
        res = res + str(k)
        num = num - k * (7**i)
        i = i - 1
    while i >= 0:
        res = res + "0"
        i = i - 1
    return res
```