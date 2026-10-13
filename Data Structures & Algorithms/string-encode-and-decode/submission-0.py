class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        words=[]
        for st in strs:
            words.append(str(len(st))+"#")
            words.append(st)
        return "".join(words)


    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            idx= s.find("#",i)
            length = int(s[i:idx])
            i= idx+length+1
            word = s[idx+1:i]
            res.append(word)
        return res
