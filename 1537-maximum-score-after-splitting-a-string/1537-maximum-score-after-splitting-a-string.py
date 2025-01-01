class Solution:
    def maxScore(self, s: str) -> int:
        ln = len(s)
        res = 0

        for i in range(1, ln):  
            left = s[:i].count('0')
            right = s[i:].count('1')
            
            score = left + right
            res = max(res, score)
        
        return res
