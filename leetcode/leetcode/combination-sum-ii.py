class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        check=set()
        def dfs(temp,indx):
            if sum(temp)==target:
                if tuple(temp) not in check:
                    ans.append(temp[:])
                check.add(tuple(temp[:]))
                return 
            if sum(temp)>target or indx>=len(candidates):
                return
            visited = set()
            for i in range(indx,len(candidates)):
                if candidates[i] in visited:
                    continue
                visited.add(candidates[i])
                temp.append(candidates[i])
                dfs(temp,i+1)
                temp.pop()
        dfs([],0)
        return ans
        