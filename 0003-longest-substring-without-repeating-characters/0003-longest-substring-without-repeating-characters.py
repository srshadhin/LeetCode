class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0

        for r,v in enumerate(s):
            while v in seen:
                seen.remove(s[l])
                l+=1
            seen.add(v)
            current_len = r - l + 1
            max_len = max(max_len, current_len)
        return max_len