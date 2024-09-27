# Array

+ [Image Smoother](#image-smoother)

[comment]: <> (Stop)

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    H = len(M)
    W = len(M[0])
    res = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            k = 0
            s = 0
            for i_k in range(i-1, i+2):
                for j_k in range(j-1, j+2):
                    if 0 <= i_k < H and 0 <= j_k < W:
                        s = s + M[i_k][j_k]
                        k = k + 1
            res[i][j] = floor(s/k)
    return res
```