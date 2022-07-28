class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        rmv = []

        # store indexes which has 0
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                rmv.append(i)

        # the number of 0
        cnt = len(rmv)

        # Delete 0 from nums
        for i in range(len(rmv)):
            del nums[rmv[i]]

        # Add 0 into tail of nums
        for i in range(cnt):
            nums.append(0)
