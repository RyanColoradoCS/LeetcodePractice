# 17. Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        if digits == "":
            return []
        
        ans = []

        def dfs_helper(index, curr_comb):

            # Base case
            if index == len(digits):
                ans.append(curr_comb) # append current combination to ans
            else:
                curr_digit = digits[index]
                # Loop through each letter the current digit can represent
                for letter in phone_keypad[curr_digit]:
                    # Append current letter to the combination and move to the next index
                    dfs_helper(index + 1, curr_comb + letter)
        
        dfs_helper(0, "")
        return ans
                    
        
        
