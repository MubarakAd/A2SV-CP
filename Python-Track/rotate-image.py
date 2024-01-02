class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotate=copy.deepcopy(matrix)
        k=len(matrix)-1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[j][k]=rotate[i][j]
            k-=1
        print(matrix)
        """
        Do not return anything, modify matrix in-place instead.
        """
        