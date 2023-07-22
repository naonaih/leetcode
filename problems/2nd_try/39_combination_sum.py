class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = set()

        def backtrack(s):
            if s == target:
                cp = stack.copy()
                # 重複を排除するため、sort
                cp.sort()
                # setで管理するため、一度tuple化してsetに追加
                res.add(tuple(cp))
                return
            elif s > target:
                return

            for c in candidates:
                stack.append(c)
                backtrack(s + c)
                stack.pop()

        backtrack(0)
        res2 = list(res)
        return res2
