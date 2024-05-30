# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        total=0
        def dfs(row,col):
            ans=0
            for r,c in dir:
                new_row=r+row
                new_col=c+col
                if inbound(new_row,new_col) and grid[new_row][new_col]>0:
                    val = grid[new_row][new_col]
                    grid[new_row][new_col] = 0
                    ans+=val + dfs(new_row,new_col)
            return ans
            
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0:
                    val=grid[i][j]
                    grid[i][j]=0
                    temp=val+dfs(i,j)
                    total= max(total,temp)
        
        
        return total
                
    
        