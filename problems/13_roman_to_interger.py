class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        cur = 0
        ans = 0
        while cur < l:
            if s[cur] == 'M':
                ans += 1000
                cur += 1
            elif s[cur] == 'D':
                ans += 500
                cur += 1
            elif s[cur] == 'C':
                if cur == l-1:
                    ans += 100
                    break
                if s[cur+1] == 'D':
                    ans += 400
                    cur += 2
                elif s[cur+1] == 'M':
                    ans += 900
                    cur += 2
                else:
                    ans += 100
                    cur += 1
                    
            elif s[cur] == 'L':
                ans += 50
                cur += 1
            elif s[cur] == 'X':
                if cur == l-1:
                    ans += 10
                    break
                if s[cur+1] == 'L':
                    ans += 40
                    cur += 2
                elif s[cur+1] == 'C':
                    ans += 90
                    cur += 2
                else:
                    ans += 10
                    cur += 1
            
            elif s[cur] == 'V':
                ans += 5
                cur += 1
            elif s[cur] == 'I':
                if cur == l-1:
                    ans += 1
                    break
                if s[cur+1] == 'V':
                    ans += 4
                    cur += 2
                elif s[cur+1] == 'X':
                    ans += 9
                    cur += 2
                else:
                    ans += 1
                    cur += 1
        return ans