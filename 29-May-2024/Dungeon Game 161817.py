# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        directions = [[0,1] ,[1,0]]

        endRow,endCol = len(dungeon),len(dungeon[0])
        def inbound(row,col):
            return  0 <= row < endRow and 0 <= col < endCol

        memo = {}
        def dfs(row,col):
            if row == endRow - 1 and col == endCol - 1 :
                if dungeon[row][col] >= 0:
                    return 1
                else:
                    return -dungeon[row][col] + 1
                
            if (row,col) not in memo:
                ans = float("inf")
                for dRow,dCol in directions:
                    newRow = dRow + row
                    newCol = dCol + col
                    if inbound(newRow,newCol):
                        minVal = dfs(newRow,newCol)
                        if minVal <= dungeon[row][col]:
                            ans = min(ans,1)
                        else:
                            ans = min(ans,minVal-dungeon[row][col])
                memo[(row,col)]  = ans
            return  memo[(row,col)] 

        return dfs(0,0)
