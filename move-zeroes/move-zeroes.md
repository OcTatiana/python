# Array

+ [Move Zeroes](#move-zeroes)

[comment]: <> (Stop)

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    k = 0
    while k < len(nums):
        if nums[i] == 0:
            nums.append(0)
            del nums[i]
            i = i - 1
        i = i + 1
        k = k + 1
```