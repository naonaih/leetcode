# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans

        def levelcheck(node, dep, parity):

            # if no value exists in curent level, add empty list for current level.
            if len(ans) == dep:
                ans.append([])

            if parity % 2 == 0:
                ans[dep] = ans[dep] + [node.val]
            else:
                ans[dep] = [node.val] + ans[dep]

            if node.left:
                levelcheck(node.left, dep + 1, parity + 1)
            if node.right:
                levelcheck(node.right, dep + 1, parity + 1)

        levelcheck(root, 0, 0)

        return ans
