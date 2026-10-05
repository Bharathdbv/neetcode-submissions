class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_vol = min(heights[i],heights[j]) * (j-i)
        while i<j:
            # curr_vol = min(heights[i],heights[j]) * (j-i)
            if heights[i] < heights[j]:
                x = heights[i]
                while heights[i] <= x and i < j:
                    i +=1
                curr_vol = min(heights[i],heights[j]) * (j-i)
                max_vol = max(max_vol, curr_vol)
            else:
                print(j)
                y = heights[j]
                while heights[j] <= y and j>i :
                    j -= 1
                curr_vol = min(heights[i],heights[j]) * (j-i)
                max_vol = max(max_vol, curr_vol)
        
        return max_vol