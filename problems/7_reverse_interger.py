class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        minus = False
        x = list(str(x))
        if len(x) == 1:
            return x[0]
        for i in range(len(x)):
            if x[i] == '-':
                minus = True
            else:
                ans = x[i] + ans
        
        ans = int(ans)
        
        if minus:
            ans = ans * (-1)
        
        if ans > 2**31-1 or ans < -(2**31):
            ans = 0
        return ans