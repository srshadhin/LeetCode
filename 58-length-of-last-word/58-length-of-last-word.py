class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        length_of_last_word = len(word[-1])
        return length_of_last_word