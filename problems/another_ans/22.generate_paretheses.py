class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # answer using DFS
        cur = ''
        res = []

        def dfs(cur, openN, closeN):
            # base case
            if openN == closeN == n:
                res.append(cur)
                return

            # case that you can add open sign
            if openN < n:
                dfs(cur + '(', openN + 1, closeN)

            # case you cna add close sign
            if closeN < openN:
                dfs(cur + ')', openN, closeN + 1)

        dfs(cur, 0, 0)
        return res
