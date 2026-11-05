# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS solotion
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count=0
        q= collections.deque([(root,root.val)])
        while q:
            node, maxval= q.popleft()
            if node:
                if node.val>=maxval:
                    count+=1
                maxval=max(maxval,node.val)
                q.append((node.left,maxval))
                q.append((node.right,maxval))
        return count

        