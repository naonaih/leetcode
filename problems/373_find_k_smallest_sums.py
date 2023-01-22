from heapq import *

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        ans = []
        if not nums1 or not nums2:
            return ans

        visited = set()
        visited.add((0,0))
        heap = []

        # Arguments for heap are following
        # val1 -> sum of 2 arrays
        # val2 -> index of nums1
        # val3 -> index of nums3
        heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while len(ans) < k and heap:

            _, i, j = heappop(heap)
            ans.append((nums1[i], nums2[j]))

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heappush(heap, (nums1[i+1]+nums2[j], i+1,j))

            if j + 1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heappush(heap, (nums1[i] + nums2[j+1], i, j+1))

        return ans
