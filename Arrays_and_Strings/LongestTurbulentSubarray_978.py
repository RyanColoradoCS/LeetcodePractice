# 978. Longest Turbulent Subarray
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        if n == 1:
            return 1

        curr_max = 1
        glob_max = 1
        prev = ""
        l = 0

        for r in range(1, n):
            if arr[r - 1] > arr[r] and prev != ">":
                curr_max = r - l + 1
                glob_max = max(curr_max, glob_max)
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                curr_max = r - l + 1
                glob_max = max(curr_max, glob_max)
                prev = "<"
            else:
                # Handle equal elements or when the pattern breaks
                if arr[r - 1] == arr[r]: 
                    l = r  # Reset window at the current index if equal consecutively
                else:
                    l = r - 1  # Pattern breaks, start from r-1
                # get prev
                if arr[r - 1] > arr[r]:
                    prev = ">"
                elif arr[r - 1] < arr[r]:
                    prev = "<"
                else:
                    prev = "="

        return glob_max

        
