class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using Kadane's Algorithm
        max_subarray = nums[0]
        max_at_current = nums[0]

        for i in range(1, len(nums)):
            max_at_current = max(nums[i], max_at_current + nums[i])
            max_subarray = max(max_subarray, max_at_current)

        return max_subarray
        
