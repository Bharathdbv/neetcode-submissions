class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        print(anagrams)
        print(anagrams.values)
        return list(anagrams.values())

