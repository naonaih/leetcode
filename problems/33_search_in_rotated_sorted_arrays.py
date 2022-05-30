class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right - left > 1:
            mid = (left + right) // 2
            print(left, right)
            if nums[mid] == target: return mid

            if nums[mid] > nums[right]:  # left part is sorted
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:  # right part is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        else:
            return -1