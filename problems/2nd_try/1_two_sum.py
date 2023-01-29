class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter(nums)
        print(c)
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in c:
                j = nums.index(diff)
                if i == j:
                    continue
                return [i,j]