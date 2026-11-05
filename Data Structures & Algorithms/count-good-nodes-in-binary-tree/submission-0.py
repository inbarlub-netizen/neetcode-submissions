# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good(root, maxval):
            if root is None:
                return 0
            res = 1 if root.val>= maxval else 0
            maxval= max(maxval, root.val)
            res+= count_good( root.left,maxval)
            res+= count_good(root.right,maxval)
            return res
        if root is None:
            return 0
        return count_good(root, root.val)

        