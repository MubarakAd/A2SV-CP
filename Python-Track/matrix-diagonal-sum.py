class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i==j:
                    _sum+=mat[i][j]
                elif i+j==len(mat)-1:
                    _sum+=mat[i][j]
        return _sum
        