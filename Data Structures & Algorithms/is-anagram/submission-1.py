class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # str1 = sort(s)
        # str2 =sort(t)
        return sorted(s) == sorted(t)
        