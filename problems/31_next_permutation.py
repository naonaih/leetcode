class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #Step1:nums[k] < nums[k+1]となる最大のkを探す
        k = -1
        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                k = i
                break
            i -= 1

        #kが-1のままであれば、すべて逆順にならんでいるので、反転して終了
        if k == -1:
            nums.reverse()
            return nums

        #Step2:k以降でnums[k] < nums[l]をみたす最大のlを求める
        l = k+1
        i = len(nums)-1
        while i > k+1:
            if nums[k] < nums[i]:
                l = i
                break
            i -= 1

        #nums[k]とnums[i]を入れ替え
        nums[k], nums[i] = nums[i], nums[k]

        #Step3:nums[k]より右かわの要素を反転
        nums[k+1:] = reversed(nums[k+1:])

        return nums
