class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # countの種類ごとにlistを作る
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a...z

            for c in s:
                # aからの相対的な位置をkeyとする
                count[ord(c)-ord('a')] += 1


            # listはmutableなため、keyにはできないので、tupleにする。
            res[tuple(count)].append(s)

        return res.values()