class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len=0
        l=0
        map={}
        for r in range(len(s)):
            map[s[r]]= 1+ map.get(s[r],0)
            most_freq=max(map.values())
            to_change= (r-l+1)-most_freq
            while to_change>k:
                map[s[l]]-=1
                l+=1
                most_freq=max(map.values())
                to_change= (r-l+1)-most_freq
            max_len= max(max_len, r-l+1)
                

        return max_len
            
        