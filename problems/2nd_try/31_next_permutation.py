class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Step1 : nums[k] < nums[k+1]となる最大のkを探す
        i = n - 2
        k = -1
        while i >= 0:
            if nums[i] < nums[i + 1]:
                k = i
                break
            i -= 1

        # k　= -1の場合は、全て逆順で並んでいるので、sortして終了
        if k == -1:
            nums.sort()
            return

        # Step2: k以降でnums[k] < nums[l]となる最大のlを探す。
        # Step1でk以降は降順に並んでいることは保証されているので、最大のlのnums[l]が最小の値となる。
        l = n - 1
        while l > k:
            if nums[k] < nums[l]:
                nums[k], nums[l] = nums[l], nums[k]
                break
            l -= 1

        # Step3: k+1以降を昇順にsortする。
        # メモ：reversedはiterlaterを返し、sortedはlistを返す
        # nums[k+1:] = reversed(nums[k+1:])
        nums[k+1:] = sorted(nums[k+1:])

