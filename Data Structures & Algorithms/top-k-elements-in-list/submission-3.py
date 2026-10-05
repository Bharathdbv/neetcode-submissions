class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1

        freq = sorted(hmap.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in freq[:k]]