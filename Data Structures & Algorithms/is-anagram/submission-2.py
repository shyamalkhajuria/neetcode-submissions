class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = defaultdict(int)
        hash_map2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for word in s :
            hash_map[word] += 1
        for word2 in t :
            hash_map2[word2] += 1
        if hash_map == hash_map2:
            return True
        return False
        
        