# 22. Generate Parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        curr = ""
        ans = []
        
        def dfs_helper(curr):
            # base case:
            if len(curr) == (n*2):
                ans.append(curr)
                return
                
            count_open = curr.count('(')
            count_closed = curr.count(')')
            if count_open < n:
                dfs_helper(curr + "(")
            if count_closed < count_open:
                dfs_helper(curr + ")")
                
        dfs_helper(curr)
        return ans
