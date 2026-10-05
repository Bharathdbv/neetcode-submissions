class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        nl = []
        for n in nums:
            if n not in nl:
                nl.append(n)
        max_len = 1
        i=0
        while i< len(nl)-1:
            j= i+1
            curr_len = 1
            while j<len(nl) and nl[j] - nl[j-1] == 1  :
                curr_len += 1
                j +=1
            max_len = max(curr_len,max_len)
            i = j
        if len(nl) == 0:
            return 0
        return max_len