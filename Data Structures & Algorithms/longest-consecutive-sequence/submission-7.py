
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        iset = set(nums)
        maxi = 0

        for x in iset:
            if x - 1 not in iset:
                curr = 1
                k = x

                while k + 1 in iset:
                    curr += 1
                    k += 1

                maxi = max(maxi, curr)

        return maxi
