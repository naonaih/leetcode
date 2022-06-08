class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        used = [False for _ in range(len(nums))]
        track = []

        def back_track(nums, track, used):

            if len(track) == len(nums):
                dummy = track.copy()
                ans.append(dummy)
                return

            for i in range(len(nums)):
                if used[i] == True:
                    continue

                track.append(nums[i])
                used[i] = True
                back_track(nums, track, used)
                used[i] = False
                track.pop(-1)

        back_track(nums, track, used)
        # return result
        return ans




