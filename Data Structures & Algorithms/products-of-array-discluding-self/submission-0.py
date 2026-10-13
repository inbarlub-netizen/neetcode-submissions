class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        multy=1
        zero= False
        for num in nums:
            if num==0:
                if zero==False:
                    zero= True
                else:
                    return [0]*len(nums)
            else:
                multy = multy*num
        for num in nums:
            if zero==True:
                if num==0:
                    res.append(multy)
                else:
                    res.append(0)
            else:
                res.append(int(multy/num))
        return res