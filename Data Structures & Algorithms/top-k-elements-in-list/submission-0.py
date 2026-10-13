class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        d={}
        for n in nums:
            if n not in d:
                d[n]=0
            d[n]+=1
        freq = [[] for _ in range(len(nums)+1)]
        for key,val in d.items():
            freq[val].append(key)
        
        counter=0
        for i in range(len(nums)):
            cur= len(nums)-i
            for j in range(len(freq[cur])):
                res.append(freq[cur][j])
                counter +=1
                if counter==k:
                    return res
