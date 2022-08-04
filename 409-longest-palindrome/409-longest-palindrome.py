class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] +=1
        odd = 0
        result = 0
        for val in count.values():
            if val % 2 == 0:
                result += val
            else:
                odd = 1
                result += (val-1)
        
        return result + odd
        
        