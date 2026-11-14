class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res=[]
        cur=[]
        n=len(s)
        def rec(i):
            if i==n:
                res.append(cur.copy())
                return 
            
            for j in range(i,n):
                if self.isPal(s,i,j):
                    cur.append(s[i:j+1])
                    rec(j+1)
                    cur.pop()
        rec(0)
        return res
    
    def isPal(self,s,i,j):
        while(i<=j):
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

                
            
    

        