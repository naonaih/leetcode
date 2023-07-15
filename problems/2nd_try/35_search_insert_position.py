class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # 2分探索
        while r - l > 1:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m

        # rより大きい場合は、rの次のidxにinsert
        if target > nums[r]:
            return r + 1
        # lより小さい場合は、現時点でlのidxにinsert
        elif target <= nums[l]:
            return l

        # lとrの間の場合は、rのidxにinsert
        return r
