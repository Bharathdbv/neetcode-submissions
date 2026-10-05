class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        
        # Store value → index
        for k in range(n):
            # if nums[k] not in d:
            d[nums[k]] = k
        
        # Find complement
        for i in range(n):
            diff = target - nums[i]
            if diff in d and d[diff] != i:  # make sure not using the same element
                return [i, d[diff]]