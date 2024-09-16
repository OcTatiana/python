# String

+ [Reverse String](#reverse-string)

[comment]: <> (Stop)

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
    for i in range(len(s)//2):
        tmp = s[i]
        s[i] = s[-i-1]
        s[-i-1] = tmp
```