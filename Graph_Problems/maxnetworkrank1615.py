# 1615. Maximal Network Rank

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        edges = set()
        rank = [0] * n
        maxrank = 0

        # get set of connected roads/cities and rank
        for u, v in roads:
            rank[u] += 1
            rank[v] += 1
            edges.add((u,v))
            edges.add((v,u))
        
        for i in range(n):
            for j in range(i+1, n):
                cur_rank = rank[i] + rank[j]
                if (j,i) and (j,i) in edges:
                    cur_rank = cur_rank - 1
                maxrank = max(maxrank, cur_rank)

        return maxrank
