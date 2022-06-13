class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # Initializing our variables using the first one
        cur_array = nums[0]
        max_array = nums[0]

        # Start with the secont element because we already used the first element
        for i in range(1, n):
            cur_array = max(nums[i], cur_array + nums[i])
            max_array = max(cur_array, max_array)

        return max_array