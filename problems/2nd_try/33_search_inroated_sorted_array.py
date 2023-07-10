class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # Step1: pivot-indexを探す
        l = 0
        r = len(nums) - 1
        p_idx = -1

        while r - l > 1:
            m = (r + l) // 2
            if nums[m] > nums[m + 1]:
                p_idx = m
                break
            if nums[m] > nums[0]:
                l = m
            else:
                r = m

        # 2分探索の幅が2まで回った際に、p_idxが-1のときがあるため、(例：[5,1,3])
        if r - l == 1 and nums[l] > nums[r]:
            p_idx = l

        print(p_idx)

        # Step2: targetの位置を探す
        if p_idx == -1:
            l = 0
            r = len(nums) - 1
            while r - l > 1:
                m = (r + l) // 2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l = m
                else:
                    r = m

        else:
            if target == nums[p_idx]:
                return p_idx

            # p-idxよりも左側にtargetがある場合
            if target >= nums[0]:
                l = 0
                r = p_idx
                while r - l > 1:
                    m = (r + l) // 2
                    if target == nums[m]:
                        return m
                    elif target > nums[m]:
                        l = m
                    else:
                        r = m
            # p-idxよりも右側にtargetがある場合
            else:
                l = p_idx + 1
                r = len(nums) - 1
                while r - l > 1:
                    m = (r + l) // 2
                    if target == nums[m]:
                        return m
                    elif target > nums[m]:
                        l = m
                    else:
                        r = m

        if target == nums[l]:
            return l
        elif target == nums[r]:
            return r
        else:
            return -1
