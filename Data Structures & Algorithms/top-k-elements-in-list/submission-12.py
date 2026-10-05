class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hmap = {}

        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1

        freq = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
        # print(freq)
        i = 0 
    
        while(i<k):
            res.append(freq[i][0])
            i += 1
        # print(res)
        return res
        # return [x[0] for x in freq[:k]]