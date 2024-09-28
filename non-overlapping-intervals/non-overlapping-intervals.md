# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)

[comment]: <> (Stop)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort()
    k = intervals[0]
    res = 0
    for i in intervals[1:]:
        if i[0] < k[1]:
            if k[1] > i[1]:
                k = i
            res = res + 1
        else:
            k = i
    return res
```