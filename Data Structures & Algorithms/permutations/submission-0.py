#itration solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for n in nums:
            new_perms=[]
            for p in res:
                for i in range(len(p)+1):
                    new_p= p.copy()
                    new_p.insert(i,n)
                    new_perms.append(new_p)
            res= new_perms
        return res

        
        