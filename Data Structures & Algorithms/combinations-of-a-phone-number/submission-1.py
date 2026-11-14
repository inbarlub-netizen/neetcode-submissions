class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)== 0:
            return []
        res=[]
        cur=[]
        digs = [int(char) for char in digits]
        n= len(digs)

        map= {2:'abc',3:'def',4:'ghi',5:"jkl", 6:'nmo', 7:'pqrs', 8:'tuv',9:'wxyz'}
        def rec(i):
            if i>=n:
                cur_st= "".join(cur)
                res.append(cur_st)
                return 
            for ch in map[digs[i]]:
                cur.append(ch)
                rec(i+1)
                cur.pop()
            
        
        rec(0)
        return res
        