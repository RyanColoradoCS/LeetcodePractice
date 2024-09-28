class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        adjList = {}
        curr_path = []
        paths = []
        
        # create the adjacency list
        for src in range(len(graph)):
            # src is the current node (index of graph)
            if src not in adjList:
                adjList[src] = []
            for dst in graph[src]:
                adjList[src].append(dst)
            
        def dfs_helper(node, curr_path):
            curr_path.append(node)
            
            # if end reached, add to paths
            if node == len(graph)-1:
                paths.append(list(curr_path)) # append a copy of curr_path
            else: # go through adjacency list
                for n in adjList[node]:
                    dfs_helper(n, curr_path)
            
            curr_path.pop() # pop current node from curr_path
        
        dfs_helper(0, curr_path)
        return paths
