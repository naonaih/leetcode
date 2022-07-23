class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        interval_sorted = sorted(intervals, key=lambda x: x[0])
        pre_end = -1
        for mtg in interval_sorted:
            start = mtg[0]
            end = mtg[1]
            if pre_end > start:
                return False

            pre_end = end

        return True