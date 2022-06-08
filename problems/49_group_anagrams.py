class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(int)
        cur = 1

        ans = []
        for s in strs:
            sl = list(s)
            sl.sort()
            s2 = ''.join(sl)
            print(s2)

            if d[s2] == 0:
                d[s2] = cur
                ans.append([s])
                cur += 1
            else:
                ans[d[s2] - 1].append(s)

        return ans