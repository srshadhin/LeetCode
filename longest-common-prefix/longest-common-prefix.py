class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            result.append(i[0])
        return "".join(result)     
