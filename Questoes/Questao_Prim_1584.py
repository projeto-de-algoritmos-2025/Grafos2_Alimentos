import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost

            for v in range(n):
                if v not in visited:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, v))

        return total_cost
