# 1376. Time Needed to Inform All Employees

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        tree = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)
        
        def dfs(employee):
        # Base case: no subordinates, return 0
            if not tree[employee]:
                return 0

            # set time to return to 0
            max_time = 0

            for direct_reports in tree[employee]:
                max_time = max(max_time, dfs(direct_reports))
            
            return max_time + informTime[employee]

        return dfs(headID)
        
