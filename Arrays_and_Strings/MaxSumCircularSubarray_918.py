# 918. Maximum Sum Circular Subarray

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr_sum = sum(nums)

        # Using Kadane's Algorithm to get max
        max_subarray = nums[0]
        max_at_current = nums[0]
        min_subarray = nums[0]
        min_at_current = nums[0]

        for index in range(1, n):

            max_at_current = max(nums[index], max_at_current + nums[index])
            max_subarray = max(max_subarray, max_at_current)

            min_at_current = min(nums[index], min_at_current + nums[index])
            min_subarray = min(min_subarray, min_at_current)

        if max_subarray < 0:
            return max(nums)

        # arr_sum - min_subarray finds the longest subarray that uses 
        # the circular trait of the array
        # this compares the max subarray of non-circular and circular and returns that
        if max_subarray > arr_sum - min_subarray:
            return max_subarray
        else:
            return arr_sum - min_subarray
