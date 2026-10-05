class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        for n in nums:
            summ += n
        tobe = (len(nums) * (len(nums) + 1)) // 2
        return tobe - summ