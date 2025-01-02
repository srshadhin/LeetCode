class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels

        n = len(words)
        prefix = [0] * n
        prefix[0] = 1 if is_vowel_string(words[0]) else 0
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + (1 if is_vowel_string(words[i]) else 0)

        result = []
        for l, r in queries:
            if l == 0:
                result.append(prefix[r])
            else:
                result.append(prefix[r] - prefix[l - 1])

        return result