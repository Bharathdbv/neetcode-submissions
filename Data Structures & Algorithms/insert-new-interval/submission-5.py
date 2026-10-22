
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < newInterval[0]:
                left = mid + 1
            else:
                right = mid
        start_idx = left

        left, right = start_idx, n
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][0] <= newInterval[1]:
                left = mid + 1
            else:
                right = mid
        end_idx = left

        start = newInterval[0]
        end = newInterval[1]

        for i in range(start_idx, end_idx):
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])

        return intervals[:start_idx] + [[start, end]] + intervals[end_idx:]




# class Solution:

#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         i=0
#         res = []
#         while i<len(intervals) and intervals[i][1] < newInterval[0]:
#             res.append(intervals[i])
#             i += 1
#         minv = newInterval[0]
#         maxv = newInterval[1]

#         while i< len(intervals) and newInterval[1] >= intervals[i][0]:
#             minv = min(minv, intervals[i][0])
#             maxv = max(maxv, intervals[i][1])
#             i += 1
#         res.append([minv,maxv])

#         while i< len(intervals):
#             res.append(intervals[i])
#             i+=1
        
#         return res


    # insert the new interval maintaining sorted order and call the merge function

    
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     i = 0 
    #     n = len(intervals)
    #     if n == 0:
    #         return [newInterval]
    #     while i<n:
    #         if newInterval[0] <= intervals[i][0]:
    #             intervals.insert(i,newInterval)
    #             break
    #         i += 1
    #     if n == len(intervals):
    #         intervals.append(newInterval)
    #     return self.merge(intervals)


    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     intervals.sort(key=lambda x: x[0])
    #     if len(intervals) == 0 or len(intervals) == 1:
    #         return intervals
    #     else:
    #         result = []
    #         result.append(intervals[0])
    #         for i in range(1,len(intervals)):
    #             if intervals[i][0] <= result[-1][1]:
    #                 x = [result[-1][0] , max(intervals[i][1] , result[-1][1])]
    #                 result.pop()
    #                 result.append(x)
    #             else:
    #                 result.append(intervals[i])
    #         return result


    
