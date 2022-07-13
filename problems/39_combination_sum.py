class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur_list, cur_sum, start):
            if cur_sum == target:
                # makes a deep copy of the current list
                ans.append(cur_list[:])
            # if the sum exceeds the target value, the current list cannot be candidate
            elif cur_sum > target:
                return

            for j in range(start, n):
                cur_list.append(candidates[j])
                # give the curent number another chance.
                backtrack(cur_list, cur_sum + candidates[j], j)

                # backtrack, remove the number from the list
                cur_list.pop()

        n = len(candidates)
        ans = []
        backtrack([], 0, 0)

        return ans