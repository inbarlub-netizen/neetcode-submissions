# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_height(root):
            if root is None:
                return 0
            left = calc_height(root.left)
            if left==-1:
                return -1
            right= calc_height(root.right)
            if right==-1:
                return -1
            if abs(right-left)>1:
                return -1
            return 1+max(left,right)
        return calc_height(root)!=  -1

        
        