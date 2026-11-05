# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_sub(root, subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            return (root.val==subroot.val) and check_sub(root.left,subroot.left) and check_sub(root.right,subroot.right)
        
        if root is None:
            return False
        return check_sub(root, subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        