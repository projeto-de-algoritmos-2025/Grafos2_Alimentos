class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        visited_global = [False] * n  
        timestamp = {}  
        time = 0 
        res = -1 

        def dfs(node, tmap, start_time):
            nonlocal time, res
            timestamp[node] = time
            tmap[node] = time  
            time += 1

            neighbor = edges[node]
            if neighbor != -1:
                if neighbor not in timestamp:
                    dfs(neighbor, tmap, start_time)
                elif neighbor in tmap:
                    cycle_len = timestamp[node] - timestamp[neighbor] + 1
                    res = max(res, cycle_len)

            tmap.pop(node)  
            visited_global[node] = True  

        for i in range(n):
            if not visited_global[i]:
                dfs(i, {}, time)

        return res
