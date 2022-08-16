class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque

        g = [[] for i in range(n)]
        done = [False] * n

        for i in range(len(edges)):
            a = edges[i][0]
            b = edges[i][1]
            g[a].append(b)
            g[b].append(a)

        ans = 0

        # BFS which begins from each node.
        for i in range(n):
            if done[i]:
                continue

            d = deque()
            d.append(i)
            ans += 1

            while d:
                cur = d.popleft()
                done[cur] = True
                for v in g[cur]:
                    if done[v]:
                        continue
                    d.append(v)
        return ans