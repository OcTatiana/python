# String

+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)

[comment]: <> (Stop)

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
    vow = ""
    res = ""
    vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
    for el in s:
        if el in vowels:
            vow += el
    vow = vow[::-1]
    j = 0
    for el in s:
        if el in vowels:
            res += vow[j]
            j += 1
        else:
            res += el
    return res
```