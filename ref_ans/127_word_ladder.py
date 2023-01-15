import collections
import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        is_visit = set([beginWord])
        q = deque([beginWord])

        ans = 1

        while q:
            # 階層ごとにqから取り出す
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in is_visit:
                            is_visit.add(nei_word)
                            q.append(nei_word)
            ans += 1

        return 0