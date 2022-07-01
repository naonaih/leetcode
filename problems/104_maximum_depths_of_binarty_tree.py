# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # For a corner case if empty tree is given
        if root == None:
            return 0

        def dfs(node, dep):
            self.ans = max(self.ans, dep)
            if node.left:
                dfs(node.left, dep + 1)
            if node.right:
                dfs(node.right, dep + 1)

        # Begins dfs from the root node
        dfs(root, 1)
        return self.ans