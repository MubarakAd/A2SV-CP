class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        def dfs(temp,indx):
            if len(temp)==k and sum(temp)==n:
                ans.append(temp[:])
                return
            if sum(temp)>n:
                return 
            for i in range(indx,10):
                temp.append(i)
                dfs(temp,i+1)
                temp.pop()
        dfs([],1)
        return ans               
        