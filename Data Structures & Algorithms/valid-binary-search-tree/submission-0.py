# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,top, bottom):
            if root is None:
                return True
            return (bottom<root.val<top) and valid(root.left,root.val, bottom) and valid(root.right, top ,root.val )
        if root is None:
            return True
        return valid(root, float('inf'),float('-inf'))
        