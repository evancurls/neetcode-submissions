class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #this assumes the list is sorted
        intervals = sorted(intervals, key=lambda x:x[0])
        print(intervals)
        ret = []
        start = -1
        end = -1
        for interval in intervals:
            i_start, i_end = interval
            if i_start > end:
                ret.append([start,end])
                start = i_start
                end = i_end
            else:
                end = max(end, i_end)
                start = min(start, i_start)
        ret.append([start,end])
        
        return ret[1:]

        