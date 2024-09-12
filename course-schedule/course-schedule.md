# Graph

+ [Course Schedule](#course-schedule)

[comment]: <> (Stop)

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
def canFinish(self, numCourses, prerequisites):
    def dfs(node):
        if visited[node] == 1:
            return False
        visited[node] = 1
        for prereq in graph[node]:
            if visited[prereq] != 2 and dfs(prereq) is False:
                return False
        visited[node] = 2
        return True
    if len(prerequisites) == 0:
        return True
    graph = collections.defaultdict(list)
    for edge in prerequisites:
        graph[edge[1]].append(edge[0])
        graph[edge[0]]
    visited = [0] * numCourses
    for node in graph:
        if visited[node] == 0:
            if dfs(node) is False:
                return False
    return True
```