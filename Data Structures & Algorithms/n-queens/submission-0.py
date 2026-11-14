class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==0:
            return []
        cols= set()
        diag=set()
        neg_diag= set()
        res=[]
        board=[["."]*n for _ in range(n)]

        def rec(count):
            if count== n:
                cur_board= ["".join(row) for row in board]
                res.append(cur_board)
                return

            for i in range(n):
                if (i in cols) or (count+i in diag) or (count-i in neg_diag):
                    continue
                
                board[count][i]= "Q"
                cols.add(i)
                diag.add(count+i)
                neg_diag.add(count-i)
                rec(count+1)
                board[count][i]= "."
                cols.remove(i)
                diag.remove(count+i)
                neg_diag.remove(count-i)
        rec(0)
        return res

            

        