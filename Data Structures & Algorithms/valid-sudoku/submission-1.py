class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        sqr=[set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val= board[i][j]
                if  val == ".":
                    continue
                if val in row[i] or val in col[j] or val in sqr[(i//3)*3 +(j//3)] :
                    return False
                else:
                    row[i].add(val)
                    col[j].add(val)
                    sqr[(i//3)*3 +(j//3)].add(val)
        return True

            
        