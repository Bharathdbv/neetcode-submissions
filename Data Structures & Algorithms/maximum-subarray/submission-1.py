import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        max_sum = -sys.maxsize - 1
        while i< len(nums) :
            j = i
            curr_sum = nums[i]
            while j<len(nums):
                if j !=i:
                    curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
                j +=1
            i += 1
        return max_sum