# Graph

+ [Is Graph Bipartite?](#is-graph-bipartite)

[comment]: <> (Stop)

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
def isBipartite(self, graph):
    def bfs(node):
        queue = []
        queue.append(node)
        color[node] = 1
        while queue:
            cur_node = queue.pop(0)
            cur_col = color[cur_node]
            for nei in graph[cur_node]:
                if color[nei] == cur_col:
                    return False
                else:
                    if color[nei] == -1:
                        queue.append(nei)
                        color[nei] = cur_col % 2 + 1
    color = dict()
    for i in range(len(graph)):
        color[i] = -1
    for node in range(len(graph)):
        if color[node] == -1:
            if bfs(node) is False:
                return False
    return True
```