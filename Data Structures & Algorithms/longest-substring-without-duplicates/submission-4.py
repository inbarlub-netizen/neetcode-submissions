class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        max_len=0
        curr= set()
        cur_len=0
        while(r<len(s)):
            if s[r] not in curr:
                curr.add(s[r])
                cur_len+=1
                max_len= max(max_len,cur_len)
                r+=1
            else:
                while(s[l]!=s[r]):
                    curr.remove(s[l])
                    l+=1
                    cur_len-=1
                curr.remove(s[l])
                l+=1
                cur_len-=1
        return max_len


        