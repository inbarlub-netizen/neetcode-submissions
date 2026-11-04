# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def is_equal(root, subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            return (root.val==subroot.val) and is_equal(root.left,subroot.left) and is_equal(root.right,subroot.right)
        if is_equal(root,subRoot):
            return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

        