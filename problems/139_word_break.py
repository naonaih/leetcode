class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s) + 1):
            for w in wordDict:
                if i - len(s) >= 0 and s[i - len(s):i] == w:
                    dp[i] = dp[i - len(s)]
                if dp[i]:
                    break

        return dp[len(s)]

