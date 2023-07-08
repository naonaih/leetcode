class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        res = []
        cur = 0
        for s in strs:
            # sを一度sortした後にstrに変換する
            s_sorted = sorted(s)
            s_sorted_str = ''.join(s_sorted)

            # 同じアナグラムが既出の場合
            if s_sorted_str in d:
                # 管理されているindexを取得して、そのindexのリストに追加
                idx = d[s_sorted_str]
                res[idx].append(s)
            # 同じアナグラムが初めて出る場合
            else:
                # アナグラムをkeyにしてリストのindexを管理する
                d[s_sorted_str] = cur
                cur += 1
                # リストにsを追加
                res.append([s])
        return res