class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cons= set(nums)
        max_len=0
        for n in nums:           
            cur=n
            cur_len=1
            if cur-1 not in cons:   
                while cur+1 in cons:
                    cur_len +=1
                    cur=cur+1

            max_len=max(cur_len,max_len)
        return max_len
        
        