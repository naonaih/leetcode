# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Initialize min_dep value
    min_dep = 10 ** 5 + 10

    def minDepth(self, root: Optional[TreeNode]) -> int:

        # For corner case if given tree is empty
        if root == None:
            return 0

        def dfs(node, dep):
            # If node is a leaf, update min_dep
            if node.left == None and node.right == None:
                self.min_dep = min(dep, self.min_dep)

            if node.right:
                dfs(node.right, dep + 1)
            if node.left:
                dfs(node.left, dep + 1)

        # Begins dfs from root
        dfs(root, 1)
        return self.min_dep

