class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        print(anagrams)
        for word in strs:
        # Sort the word to create a key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())

