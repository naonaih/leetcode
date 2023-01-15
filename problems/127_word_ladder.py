#答えは合っているが、TLE

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def cal_dist(word1, word2):
            dist = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    dist + -1

            return dist

        wordList.append(beginWord)
        l = len(wordList)
        g = [[] for _ in range(l)]

        # Create graph which connects node which differs by only 1 letter
        for i in range(l - 1):
            for j in range(i, l):
                dist = cal_dist(wordList[i], wordList[j])
                if dist == 1:
                    g[i].append(j)
                    g[j].append(i)


        def backtrack(cur_list, cur_word):

            if cur_word == endWord:
                ans = max(ans, len(cur_list))

            for v in g[wordList.index(cur_word)]:
                if wordList[v] in cur_list:
                    continue
                else:
                    cur_list.append(wordList[v])
                    backtrack(cur_list, wordList[v])
                    cur_list.pop()



        cur_list = [beginWord]
        ans = 0
        backtrack(cur_list, beginWord)

        return ans