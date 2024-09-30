class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        curr = []

        def dfs_helper(curr):

            # Base case
            if len(curr) == len(nums):
                ans.append(curr[:])
            else:
                for num in nums:
                 if num not in curr:
                    curr.append(num)
                    dfs_helper(curr)
                    curr.pop()

        dfs_helper(curr)
        return ans
