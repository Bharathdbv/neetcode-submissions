class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inset = set()
        l = 0
        r=0
        max_len = 0

        while r<len(s):
            while s[r] in inset:
                inset.remove(s[l])
                l +=1
            
            inset.add(s[r])
            max_len = max(max_len,r-l+1)
            r += 1
        
        return max_len