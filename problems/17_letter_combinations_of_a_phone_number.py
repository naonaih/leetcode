class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        ans = []

        mp = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        dl = list(digits)

        if len(dl) == 0:
            return []
        else:
            i = 0
            while i < len(dl):
                if len(ans) == 0:
                    ans = mp[dl[i]]
                else:
                    ans = self.permutation(ans, mp[dl[i]])
                i += 1

            return ans

    def permutation(self, ls1, ls2):
        res = []
        for i in ls1:
            if len(ls2) > 0:
                for j in ls2:
                    res.append(i + j)
            else:
                res.append(i)
        return res
