class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i,temp,total):
            if total==target:
                res.append(temp[:])
                return
            
            if i>=len(candidates) or total>target:
                return
            temp.append(candidates[i])
            dfs(i,temp,total+candidates[i])
            temp.pop()
            dfs(i+1,temp,total)
        dfs(0,[],0)
        return res


        