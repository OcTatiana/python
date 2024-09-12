# Graph

+ [Course Schedule II](#course-schedule-ii)

[comment]: <> (Stop)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
def findOrder(self, numCourses, prerequisites):
    def dfs(node):
        if visited[node] == 1:
            return False
        visited[node] = 1
        for prereq in graph[node]:
            if visited[prereq] != 2 and dfs(prereq) is False:
                return False
        visited[node] = 2
        res.insert(0, node)
        return True
    if len(prerequisites) == 0:
        return [i for i in range(numCourses)]
    res = []
    graph = collections.defaultdict(list)
    for edge in prerequisites:
        graph[edge[1]].append(edge[0])
        graph[edge[0]]
    visited = [0] * numCourses
    for node in graph:
        if visited[node] == 0:
            if dfs(node) is False:
                return []
    for i in range(numCourses):
        if i not in res:
            res.append(i)
    return res
```