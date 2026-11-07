class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        top=len(matrix)-1
        bottom= 0
        n=len(matrix[0])-1
        line=-1
        while bottom <= top:
            mid= (bottom+top)//2
            if  matrix[mid][0]<=target<=matrix[mid][n]:
                line= mid
                break
            elif target < matrix[mid][0]:
                top= mid-1
            else:
                bottom=mid+1
        if line==-1:
            return False
        left,right= 0,n
        while left<=right:
            mid= (left+right)//2
            if matrix[line][mid]==target:
                return True
            elif matrix[line][mid]<target:
                left= mid+1
            else:
                right=mid-1
        return False
               
        