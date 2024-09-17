# String

+ [To Lower Case](#to-lower-case)

[comment]: <> (Stop)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
    res = ""
    for el in str:
        if 'A' <= el <= 'Z':
            res = res + chr(ord(el) + 32)
        else:
            res = res + el
    return res
```