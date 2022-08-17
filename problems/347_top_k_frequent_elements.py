class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)

        cnt = 0
        ans = []
        for cm in c.most_common():
            ans.append(cm[0])
            cnt += 1
            if cnt == k:
                break

        return ans
