# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1, node2):
            if node1 and node2:
                # If both of node exists, combine sums up their values
                root = TreeNode(node1.val + node2.val)

                # Add its children by joining rach children of both of nodes
                root.left = dfs(node1.left, node2.left)
                root.right = dfs(node1.right, node2.right)

                # Finally, return the super node
                return root
            else:
                return node1 or node2

        # Start dfs from both of head node
        return dfs(root1, root2)