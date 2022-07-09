# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False

        if root.left == None and root.right == None and root.val == targetSum:
            return True

        def dfs(node, v):
            print(v + node.val)
            if node.left == None and node.right == None and v + node.val == targetSum:
                self.ans = True
            if node.left:
                dfs(node.left, v + node.val)
            if node.right:
                dfs(node.right, v + node.val)

        if root.left:
            dfs(root.left, root.val)

        if root.right:
            dfs(root.right, root.val)
        return self.ans