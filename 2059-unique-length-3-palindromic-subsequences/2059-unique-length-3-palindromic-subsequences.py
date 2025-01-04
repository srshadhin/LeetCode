class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        from collections import defaultdict

        char_positions = defaultdict(list)
        for i, char in enumerate(s):
            char_positions[char].append(i)

        unique_palindromes = set()

        for char, positions in char_positions.items():
            if len(positions) > 1:
                left, right = positions[0], positions[-1]
                middle_chars = set(s[left + 1:right])
                for mid_char in middle_chars:
                    unique_palindromes.add((char, mid_char, char))

        return len(unique_palindromes)