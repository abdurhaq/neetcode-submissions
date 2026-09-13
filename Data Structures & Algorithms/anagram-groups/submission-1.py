class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter, defaultdict
        groups = defaultdict(list)
                      
        for word in strs:
            counts = Counter(word)
            key = tuple(sorted(Counter(word).items()))
            groups[key].append(word)
    
        return list(groups.values())