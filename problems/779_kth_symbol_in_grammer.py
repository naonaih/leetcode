class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solver(n, k):
            if n == 1:
                return 0
            mid = 2 ** (n - 2)
            if k > mid:
                return 1 - solver(n - 1, k - mid)
            else:
                return solver(n - 1, k)

        return solver(n, k)
