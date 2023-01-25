# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ref: https://leetcode.com/problems/split-bst/solutions/2996704/python-with-pictures/?orderBy=most_votes

class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def cut(node):
            if not node:
                return None, None

            if node.val <= target:
                left, right = cut(node.right)
                node.right = left
                return node, right

            elif node.val > target:
                left, right = cut(node.left)
                node.left = right
                return left, node

        return cut(root)