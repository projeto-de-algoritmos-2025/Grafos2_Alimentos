import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        grafo = {i: [] for i in range(1, n + 1)}
        for de_no, para_no, times in times:
            grafo[de_no].append((para_no, times))
        
        distancias = {i: float('inf') for i in range(1, n + 1)}
        distancias[k] = 0
        fila = [(0, k)]
        
        while fila:
            times_atual, no = heapq.heappop(fila)
            if times_atual > distancias[no]:
                continue
            for vizinho, times in grafo[no]:
                novo_times = times_atual + times
                if novo_times < distancias[vizinho]:
                    distancias[vizinho] = novo_times
                    heapq.heappush(fila, (novo_times, vizinho))
        
        times_maximo = max(distancias.values())
        return times_maximo if times_maximo != float('inf') else -1
