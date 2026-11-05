# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        q= collections.deque([root])
        while q:
            length= len(q)
            found = False
            for i in range(length):
                
                node= q.popleft()
                if node and not found:
                    res.append(node.val)
                    found=True
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res
                

        