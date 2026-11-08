# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res=[]
        q= collections.deque([root])
        while(q):
            node=q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append("none") 
            
        return ",".join(res)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        vals= data.split(",")
        root= TreeNode(int(vals[0]))
        q= collections.deque([root])
        i=1
        while q and i<len(vals):
            node= q.popleft()
            if i<len(vals):
                left=vals[i] 
                i+=1
                if left != "none":
                    node.left= TreeNode(int(left))
                    q.append(node.left)
            if i<len(vals):
                right=vals[i] 
                i+=1
                if right != "none":
                    node.right= TreeNode(int(right))
                    q.append(node.right)
        return root    


