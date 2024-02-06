class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            a_map[sorted_word].append(word)
        
        return list(a_map.values())
            
        