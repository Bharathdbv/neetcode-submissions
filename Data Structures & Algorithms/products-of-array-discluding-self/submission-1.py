class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc = 0
        np =1
        nzp = 1
        for n in nums:
            if n != 0:
                np *= n
                nzp *= n
            elif n ==0 :
                np *= n
                zc +=1
        res = []
        if zc>=2:
            return [0]*len(nums)
        else:
            for x in nums:
                if x == 0:
                    res.append(nzp)
                else:
                    res.append(np // x)

        return res