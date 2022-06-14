class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combinations_count(n, r):
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

        # if m == 1 or n == 1:
        #    ans = 1

        ans = combinations_count(m + n - 2, n - 1)

        return ans