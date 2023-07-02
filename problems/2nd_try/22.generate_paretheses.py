class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closeN):
            # base case
            if openN == closeN == n:
                res.append(''.join(stack))
                return

            # case that you can add open sign
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closeN)
                stack.pop()

            # case you cna add close sign
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
