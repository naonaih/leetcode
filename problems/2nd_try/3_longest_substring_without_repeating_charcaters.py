class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = len(s)
        s = list(s)
        cur = cnt = ans = 0
        start = 0
        s_set = set()

        def find_start(c, start):
            for i in range(start, l):
                if s[i] == c:
                    return i + 1

            return start + 1

        while cur < l:
            if s[cur] not in s_set:
                s_set.add(s[cur])
                cur += 1
                cnt += 1
            else:
                ans = max(ans, cnt)
                start = find_start(s[cur], start)
                cur = start
                cnt = 0
                s_set = set()

        ans = max(ans, cnt)
        return ans