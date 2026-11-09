class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if not nums or n<3:
            return []
        nums.sort()
        idx=0
        res=[]
        while idx<n-2 :
            while(idx>0 and nums[idx]==nums[idx-1]and idx<n-2):
                idx+=1
            l,r=idx+1,n-1
            while(l<r):
                if nums[l]+nums[r]== -(nums[idx]):
                    res.append([nums[idx],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]< -(nums[idx]):
                    l+=1
                else:
                    r-=1
            idx+=1
        return res
        