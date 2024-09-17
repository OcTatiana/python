# Array

+ [Max Consecutive Ones](#max-consecutive-ones)

[comment]: <> (Stop)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    i = 0
    l = 0
    res = 0
    while i < len(nums):
        while i < len(nums) and nums[i] == 1:
            l = l + 1
            i = i + 1
        res = max(l, res)
        l = 0
        i = i + 1
    return res
```