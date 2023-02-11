class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n == 1:
            return s

        step = 2 * n - 2

        res = ''
        for i in range(n):
            for j in range(i, len(s), step):
                # 最初の行と最後の行は、step刻みで付け足していくだけ
                res += s[j]

                # 間の行は、2 * (n - 1 - i)先の文字を追加する必要がある
                if i != 0 and i != n - 1 and j + 2 * (n - 1 - i) < len(s):
                    res += s[j + 2 * (n - 1 - i)]

        return res
