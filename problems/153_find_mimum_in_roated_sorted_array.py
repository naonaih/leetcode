# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        tail = nums[r]

        # Search inflection point by using binary serach
        while r - l > 1:
            m = (r + l) // 2
            # if middle value exceeds the tail value, inflection point should be on the right of mid
            if nums[m] > tail:
                l = m
            # if middle value does not excees the tail value, inflection point should be on the left of mid
            else:
                r = m

        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]