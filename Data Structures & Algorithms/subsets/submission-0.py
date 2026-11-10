class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        n= len(nums)
        res=[]
        def dfs(i,cur):
            if i>= n:
                res.append(cur.copy())
                return           
            dfs(i+1,cur)
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()

        dfs(0,[])
        return res

        