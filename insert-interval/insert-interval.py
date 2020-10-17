class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        intervals.append(newInterval)
        intervals.sort()
        while i < len(intervals) - 1:
            if intervals[i][-1] >= intervals[i+1][0]:
                if intervals[i+1][-1] < intervals[i][-1]:
                    intervals.append([intervals[i][0], intervals[i][-1]])
                else:
                    intervals.append([intervals[i][0], intervals[i+1][-1]])
                del intervals[i+1]
                del intervals[i]
                intervals.sort()
                i = i - 1
            i = i + 1
        intervals.sort()
        return intervals
