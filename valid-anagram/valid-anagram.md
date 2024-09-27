# String

+ [Valid Anagram](#valid-anagram)

[comment]: <> (Stop)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    for el in t:
        i = 0
        while i < len(s):
            if el == s[i]:
                s = s[:i] + s[i+1:]
                break
            if i == len(s) - 1:
                return False
            i = i + 1
    return True
```