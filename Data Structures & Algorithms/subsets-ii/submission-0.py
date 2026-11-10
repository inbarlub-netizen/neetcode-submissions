class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res=[]
        n=len(nums)
        nums.sort()
        def dfs(i,cur):
            if i==n:
                res.append(cur.copy())
                return
            if i>n:
                return
            
            cur.append(nums[i])
            dfs(i+1,cur)
            cur.pop()
            while i+1<n and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,cur)
        dfs(0,[])
        return res

        