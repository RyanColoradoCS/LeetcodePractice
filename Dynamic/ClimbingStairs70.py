class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        arr = [1, 1]
        i = 2
        
        while i <= n:
            tmp = arr[1]
            arr[1] = arr[0] + arr[1]
            arr[0] = tmp
            i += 1
        
        return arr[1]
        