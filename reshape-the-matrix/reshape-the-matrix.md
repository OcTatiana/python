# Array

+ [Reshape the Matrix](#reshape-the-matrix)

[comment]: <> (Stop)

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r * c != len(nums) * len(nums[0]):
        return nums
    res = []
    k = c
    tmp = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            tmp.append(nums[i][j])
            k -= 1
            if k == 0:
                res.append(tmp)
                tmp = []
                k = c
    return res
```