class Solution:
    def validPalindrome(self, s: str) -> bool:
        lng = len(s)
        for l in range(lng//2):
            r = lng-1-l
            if s[l]!=s[r]:
                ld, rd = s[l+1:r+1], s[l:r]
                return ld==ld[::-1] or rd==rd[::-1]
        return True