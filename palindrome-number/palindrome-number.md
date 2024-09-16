# Math

+ [Palindrome Number](#palindrome-number)

[comment]: <> (Stop)

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    x = (str)(x)
    for i in range(len(x)//2):
        if x[i] != x[-i - 1]:
            return False
    return True
```