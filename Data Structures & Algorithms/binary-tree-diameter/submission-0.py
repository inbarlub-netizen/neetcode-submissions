# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def depth(root):
            if root is None:
                return 0
            rightLen= depth(root.right)
            leftLen= depth(root.left)
            self.max_len= max(leftLen +rightLen,self.max_len )
            return 1+ max(leftLen,rightLen )
        depth(root)
        return self.max_len
        