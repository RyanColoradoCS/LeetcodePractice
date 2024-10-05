class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        max_subarray = sum(nums[:k])
        current = sum(nums[:k])

        for i in range(k, len(nums)):
            current = current + nums[i] - nums[i-k]
            max_subarray = max(max_subarray, current)

        return (max_subarray*1.0)/k
