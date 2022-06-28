# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans

        def levelcheck(node, dep):

            # if no value exists in curent level, add empty list for current level.
            if len(ans) == dep:
                ans.append([])

            ans[dep].append(node.val)

            # process child node for the next level.
            if node.left:
                levelcheck(node.left, dep + 1)
            if node.right:
                levelcheck(node.right, dep + 1)

        levelcheck(root, 0)

        return ans