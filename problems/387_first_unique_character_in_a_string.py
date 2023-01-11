class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections

        INF = 10 ** 6
        s = list(s)

        c = collections.Counter(s)
        ans = INF

        for item in c.items():
            print(item)
            if item[1] == 1:
                ans = min(ans, s.index(item[0]))

        # If there is no character which does not repeat.
        if ans == INF:
            ans = -1

        return ans