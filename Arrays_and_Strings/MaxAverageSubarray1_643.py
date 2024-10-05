class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        left = curr = avg = 0
        
        length = len(nums) - 1
        curr = sum(nums[:k])
        ans = float(curr)/k
        
        i = 0
        while i <= length - k:
            curr -= nums[i]
            curr += nums[i + k]
            avg = float(curr)/k
            ans = max(ans, avg)
            i+=1
        
    
        return ans
        
