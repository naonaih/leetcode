class Solution:
    def check(self, s):
        from collections import deque
        d = deque()

        c = 0
        op = ['(', '{', '[']
        cl = [')', '}', ']']

        while c < len(s):
            if s[c] in op:
                d.append(s[c])
                c += 1
            else:
                if len(d) == 0:
                    return False
                p = d.pop()
                print(p)
                if (s[c] == ')' and p != '(') or \
                        (s[c] == '}' and p != '{') or \
                        (s[c] == ']' and p != '['):
                    return False
                else:
                    c += 1

        if len(d) > 0:
            return False

        return True

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        for bit in range(2**(n*2)):
            s = ''
            for i in range(2*n):
                if bit & 1<<i:
                    s = s + '('
                else:
                    s = s + ')'
            print(s)
            if self.check(s):
                ans.append(s)
        return ans




