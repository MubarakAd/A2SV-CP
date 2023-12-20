class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for a, b in zip(matrix, matrix[1:]):
            for x, y in zip(a, b[1:]):
                if x != y: return False
        return True