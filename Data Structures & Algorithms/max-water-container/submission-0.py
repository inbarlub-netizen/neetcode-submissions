class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r =0, len(heights)-1
        max_len=0
        while(l<r):
            height= min(heights[l],heights[r])
            cur_len= (r-l)*height
            if cur_len>max_len:
                max_len=cur_len
            if height==heights[l]:
                l+=1
            else:
                r-=1
        return max_len

        