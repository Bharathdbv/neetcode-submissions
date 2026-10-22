class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        iset = set(nums)
        sset = set()
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        maxi = -1
        for x in iset:
            if x-1 not in iset and x not in sset:
                curr = 1
                k = x
                sset.add(k)
                while k + 1 in iset:
                    curr += 1
                    k += 1
                    sset.add(k)
                maxi = max(maxi,curr)
        
        return maxi