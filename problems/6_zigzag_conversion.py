class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        n = numRows
        ans = [[] for i in range(n)]
        l = 0
        
        while l < len(s):
            for i in range(n):
                if l == len(s):
                    break
                ans[i].append(s[l])
                l += 1
            
            for j in range(n-2,0,-1):
                if l == len(s):
                    break
                ans[j].append(s[l])
                l += 1
        
        ANS = ''
        for i in range(n):
            ANS += ''.join(ans[i])
            
        return ANS
                