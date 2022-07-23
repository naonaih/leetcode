class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        cnt = [0] * (10 ** 6 + 2)
        point = []

        # Imos method
        for i in range(len(intervals)):
            cnt[intervals[i][0]] += 1
            cnt[intervals[i][1]] -= 1
            point.append(intervals[i][0])
            point.append(intervals[i][1])

        point.sort()

        room = cnt[point[0]]
        pre = point[0]
        ans = room

        # Calculate cumulative sum at trigger point.
        for i in range(1, len(point)):
            print(point[i], cnt[point[i]])
            if point[i] != pre:
                room += cnt[point[i]]
                ans = max(ans, room)
                pre = point[i]

        return ans