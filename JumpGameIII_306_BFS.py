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
        
        while queue:
            
            index = queue.popleft()
            
            if arr[index] == 0:
                return True
            
            if (index + arr[index] < n) and (index + arr[index] >= 0) and (index not in visited):
                queue.append(index + arr[index])
            
            if (index - arr[index] < n) and (index - arr[index] >= 0) and (index not in visited):
                queue.append(index - arr[index])
                
            visited.add(index)
            
        return False
        
