# Graph

+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)

[comment]: <> (Stop)

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
def findCheapestPrice(self, n, flights, src, dst, k):
    inf = 10000000
    graph = collections.defaultdict(list)
    for from_i, to_i, price_i in flights:
        graph[from_i].append((to_i, price_i))
    q = [(src, 0, 0)]  # vertex, price, stops
    cost = [inf] * n
    cost[src] = 0
    while q:
        v, price, stops = q.pop(0)
        for to_i, price_i in graph[v]:
            new_price = price + price_i
            if new_price < cost[to_i] and stops <= k:
                cost[to_i] = new_price
                q.append((to_i, new_price, stops+1))
    return cost[dst] if cost[dst] != inf else -1
```