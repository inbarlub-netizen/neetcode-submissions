class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur=[]
        def rec (openN, closeN):
            if openN==closeN == n:
                res.append("".join(cur))
            
            if openN <n:
                cur.append("(")
                rec(openN+1,closeN)
                cur.pop()

            if openN>closeN:
                cur.append(")")
                rec(openN, closeN+1)
                cur.pop()
        rec(0,0)
        return res
        