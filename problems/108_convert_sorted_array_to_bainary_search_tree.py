# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def get_root(l, r):
            if l > r:
                return None

            # always choose left middle node as a root
            p = (l + r) // 2

            root = TreeNode(nums[p])
            root.left = get_root(l, p - 1)
            root.right = get_root(p + 1, r)
            return root

        return get_root(0, len(nums) - 1)