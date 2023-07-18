class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        if len(word1) == len(word2):
            for i, d in enumerate(word1):
                result += word1[i] + word2[i]

        if len(word1) > len(word2):
            for i, d in enumerate(word1):
                if (i < len(word2)):
                    result += word1[i] + word2[i]
                else:
                    result += word1[i]

        if len(word1) < len(word2):
            for i, d in enumerate(word2):
                if (i < len(word1)):
                    result += word1[i] + word2[i]
                else:
                    result += word2[i]

        return result