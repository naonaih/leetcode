class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # corner case
        if not s:
            return True

        # current index of s
        cur = 0
        for i in range(len(t)):
            # if the index of s reaches the end of string, it means we can say True
            if s[cur] == t[i]:
                if cur == len(s) - 1:
                    return True
                # If char of s matches char of t, proceed the index of s
                cur += 1

        return False

