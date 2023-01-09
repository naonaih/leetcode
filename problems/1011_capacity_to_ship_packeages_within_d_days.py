class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def is_ok(allow_weight):
            cur_day = 1
            cur_wei = 0
            for i in range(len(weights)):
                if weights[i] > allow_weight:
                    return False
                if cur_wei + weights[i] > allow_weight:
                    cur_day += 1
                    cur_wei = weights[i]
                else:
                    cur_wei += weights[i]
            if cur_day > days:
                return False
            else:
                return True

        max_weight = sum(weights)
        l = 0
        r = max_weight
        while r - l > 1:
            m = (r + l) // 2
            if is_ok(m):
                r = m
            else:
                l = m

        return r
