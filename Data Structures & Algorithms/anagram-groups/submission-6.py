class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        
        for words in strs:
            key = "".join(sorted(words))

            if key not in mp:
                mp[key] = []

            mp[key].append(words) 

        return list(mp.values())