class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        
        slen = len(s)
        cur = 0
        while cur < slen and s[cur] == " ":
            cur += 1
        
        print(cur)
        if cur >= slen:
            return 0
        
        sign = 1
        if s[cur] == '-':
            sign = -1
        if s[cur] == '+' or s[cur] == '-':
            cur += 1
        if cur >= slen:
            return 0
        
        print(cur)
        ans = 0
        while cur < slen:
            if s[cur].isdigit():
                ans = ans * 10 + int(s[cur])
            else:
                break
            cur += 1
        
        ans *= sign
        
        if ans > 2**31-1:
            ans = 2**31-1
        if ans < -(2**31):
            ans = -(2**31)
        
        return ans
        
        