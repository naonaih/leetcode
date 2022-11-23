class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cursum = 0
        d = {0: 1}

        for n in nums:
            cursum += n

            # calculate difference between sum and target number
            diff = cursum - k

            # add occurrences counts of diff number to answer because the number matches k if we remove prefixes which sums up to sum -k
            ans += d.get(diff, 0)

            # add 1 to occurrences counts
            d[cursum] = d.get(cursum, 0) + 1

        return ans
