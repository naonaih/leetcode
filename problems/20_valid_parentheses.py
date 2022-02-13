class Solution:
    def isValid(self, s: str) -> bool:
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