class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])

        def kruskal(n, edges, include=None, exclude=None):
            uf = UnionFind(n)
            weight = 0
            if include is not None:
                u, v, w, _ = edges[include]
                if uf.union(u, v):
                    weight += w
            for i in range(len(edges)):
                if i == exclude:
                    continue
                u, v, w, _ = edges[i]
                if uf.union(u, v):
                    weight += w
            root = uf.find(0)
            for i in range(1, n):
                if uf.find(i) != root:
                    return float('inf')
            return weight

        original_weight = kruskal(n, edges)
        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            if kruskal(n, edges, exclude=i) > original_weight:
                critical.append(edges[i][3])
            elif kruskal(n, edges, include=i) == original_weight:
                pseudo_critical.append(edges[i][3])

        return [critical, pseudo_critical]
