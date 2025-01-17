class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        for word in words:
            if word.startswith(pref):
                counter += 1
        return counter