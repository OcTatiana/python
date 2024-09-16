# String

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

[comment]: <> (Stop)

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
    res = ""
    words = s.split(" ")
    for el in words:
        res += el[::-1]
        res += " "
    return res[:-1:]
```