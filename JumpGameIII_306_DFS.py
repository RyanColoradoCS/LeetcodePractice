# 306. Jump Game III

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        queue = deque([start])
        visited = set()
        
        def dfs(start):
            
            index = start
            
            if arr[index] == 0:
                return True
            
            visited.add(index)
            
            if (index + arr[index] < n) and (index + arr[index] >= 0) and (index + arr[index] not in visited):
                if dfs(index + arr[index]):
                    return True
            
            if (index - arr[index] < n) and (index - arr[index] >= 0) and (index - arr[index] not in visited):
                if dfs(index - arr[index]):
                    return True
            
            return False
        
        
        return dfs(start)
        
