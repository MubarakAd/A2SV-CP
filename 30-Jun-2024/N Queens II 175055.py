# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def IsSafe(self,row,column,n,board):
        for i in range(column):
            if board[row][i] == "Q":
                return False
        i,j = row,column
        while(i>=0 and j>=0):
            if(board[i][j] == "Q"):
                return False
            i -= 1
            j -= 1
        i,j = row,column
        while(i<n and j>=0):
            if(board[i][j] == "Q"):
                return False
            i += 1
            j -= 1
        return True
    def solveQueens(self,column,n,board,result):
        if column == n:
            result.append(["".join(i) for i in board])
            return
        for row in range(n):
            if(self.IsSafe(row,column,n,board)):
                board[row][column] = "Q"
                self.solveQueens(column+1,n,board,result)
                board[row][column] = "."
        return
    def totalNQueens(self, n: int) -> int:
        board = [["." for i in range(n)] for i in range(n)]
        result = []
        self.solveQueens(0,n,board,result)
        return len(result)