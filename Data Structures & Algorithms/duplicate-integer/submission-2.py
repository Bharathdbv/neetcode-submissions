class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        temp = False
        for i in nums:
            if i in li:
                temp = True
                break
            else:
                li.append(i)
        return temp 