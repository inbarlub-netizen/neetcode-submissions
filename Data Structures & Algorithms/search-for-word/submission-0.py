class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None:
            return False
        r_len,c_len= len(board), len(board[0])
        i=0
        path= set()
        def dfs(r,c,i):
            if i== len(word):
                return True
            if r<0 or c<0 or r>=r_len or c>= c_len or word[i]!=board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res= dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            path.remove((r,c))
            return res
        for r in range(r_len):
            for c in range(c_len):
                if dfs(r,c,0):
                    return True
        return False

