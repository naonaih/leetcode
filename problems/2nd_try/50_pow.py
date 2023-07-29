class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # ベースケース
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res

            # nが偶数の場合は、そのまま返すが、nが奇数の場合は、xを掛けて返す。
            return x * res if n % 2 == 1 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
