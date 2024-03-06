class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        left=0
        right=col*row-1
        while left<=right:
            mid=(left+right)//2
            co=mid%col
            ro=mid//col
            if matrix[ro][co]==target:
                return True
            elif matrix[ro][co]>target:
                right=mid-1
            else:
                left=mid+1
        return False


        