class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count= 0
        if grid is None or grid[0] is None:
            return 0
        res=0
        visited = set()
        nc= len(grid[0])
        nr= len(grid)
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,col = q.popleft()

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for addr,addc in directions:
                    r,c = addr+row,addc+col
                    if r in range (nr) and c in range(nc) and grid[r][c]=="1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))                         
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    res+=1
        
        return res