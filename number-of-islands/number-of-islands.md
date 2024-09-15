# Graph

+ [Number of Islands](#number-of-islands)

[comment]: <> (Stop)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
def numIslands(self, grid):
    width = len(grid[0])
    height = len(grid)
    count = 0
    def find_component(i, j):
        grid[i][j] = "0"
        for h, w in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= h < height and 0 <= w < width and grid[h][w] == "1":
                find_component(h, w)
    for i in range(height):
        for j in range(width):
            if (grid[i][j] == "1"):
                find_component(i, j)
                count += 1
    return count
```