# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#faster solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_in_idx= {val:idx for idx,val in enumerate(inorder)}
        
        def helper(p_s,p_e,in_s,in_e):

            if p_s>p_e or in_s>in_e:
                return None
            
            root= TreeNode(preorder[p_s])
            root_in_idx= map_in_idx[preorder[p_s]]
            left_size = root_in_idx - in_s

            root.left= helper(p_s+1 ,p_s+left_size , in_s,root_in_idx-1)
            root.right= helper( p_s+left_size+1 , p_e,root_in_idx+1, in_e)

            return root
        return helper(0, len(preorder)-1,0,len(inorder)-1)
        
        
        