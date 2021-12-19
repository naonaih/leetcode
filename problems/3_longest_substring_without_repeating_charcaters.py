class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        s = list(s)
        ans = 0
        cnt = 0
        cur = 0
        srt = 0
        
        while cur < len(s):
            if s[cur] not in c:
                c.add(s[cur])
                cur += 1
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 0
                srt += 1
                cur = srt
                c = set()

        ans = max(ans,cnt)
        return ans
        