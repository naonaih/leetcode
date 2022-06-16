class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Get the length of list
        n = len(nums)

        ans = []

        # Execute binary search
        for i in range(2 ** n):
            can = []
            for bit in range(n):
                # if i-th bit is 1, should add nums of i-th index into candidate
                if i & 1 << bit:
                    can.append(nums[bit])

            # Add candidate list into answer list
            ans.append(can)

        return ans