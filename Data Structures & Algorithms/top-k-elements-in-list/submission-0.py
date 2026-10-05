from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num] += 1

        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in freq_dict:
            freq = freq_dict[num]
            freq_list[freq].append(num)

        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
