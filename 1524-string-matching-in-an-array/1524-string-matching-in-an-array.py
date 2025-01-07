class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    substrings.add(words[i])
        
        return list(substrings)