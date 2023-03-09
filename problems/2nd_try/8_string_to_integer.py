class Solution:
    def myAtoi(self, s: str) -> int:

        # コーナーケース
        if s == '':
            return 0

        list_str = list(s)
        cur = 0
        sign = 0  # 符号(0の場合は、＋、１の場合は-)
        ans = ""

        # 符号が決定するまでのwhile文
        while cur < len(list_str):
            if list_str[cur] == ' ':
                cur += 1
            elif list_str[cur] == '+':
                cur += 1
                break
            elif list_str[cur] == '-':
                sign = 1
                cur += 1
                break
            elif list_str[cur].isdecimal():
                break
            else:
                return 0

        # 数字読み込みのwhile文
        while cur < len(list_str):
            if list_str[cur].isdecimal():
                ans = ans + list_str[cur]
                cur += 1
            else:
                break

        if ans == "":
            return 0

        # プラスかマイナスかを判定
        if sign == 0:
            ans = int(ans)
        elif sign == 1:
            ans = int(ans) * -1

        # 　３２bitに収まる範囲に丸める
        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        if ans < -(2 ** 31):
            ans = -(2 ** 31)

        return ans