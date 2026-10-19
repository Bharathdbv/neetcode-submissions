class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zc =0 
        for x in nums:
            if x == 0 and zc ==0 :
                zc +=1
            elif x == 0 and zc !=0 :
                prod = 0
                break
            else:
                prod *= x
        print(prod)
        print(zc)
        res = []
        if zc >1:
            return [0]*len(nums)
        else:
            for y in nums:
                if y == 0:
                    res.append(prod)
                elif zc == 0:
                    res.append(int(prod/y))
                elif zc == 1:
                    res.append(0)
            return res

        