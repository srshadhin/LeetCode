class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        n, r = len(word1), len(word2)
        res = ""
        for i in range(min(n,r)):
            res += f"{word1[i]}{word2[i]}"
            
        if n > r:
            res += word1[i+1:]
        elif r > n:
            res += word2[i+1:]
        
        return res