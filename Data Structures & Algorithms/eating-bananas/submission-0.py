class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right= 1,max(piles)
        rs= right
        while left<=right:
            k= (left+right)//2
            hours= 0
            for p in piles:
                hours+= math.ceil(p/k)
            if hours<= h:
                rs= min(rs, k)
                right=k-1
            else:
                left=k+1
        return rs
        