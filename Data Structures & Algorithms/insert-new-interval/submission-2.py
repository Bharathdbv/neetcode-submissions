class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        res = []
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        minv = newInterval[0]
        maxv = newInterval[1]

        while i< len(intervals) and newInterval[1] >= intervals[i][0]:
            minv = min(minv, intervals[i][0])
            maxv = max(maxv, intervals[i][1])
            i += 1
        res.append([minv,maxv])

        while i< len(intervals):
            res.append(intervals[i])
            i+=1
        
        return res




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
    
