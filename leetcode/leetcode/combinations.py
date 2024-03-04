class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans=[]
        def backtrack(path,start):
            if len(path)==k:
                ans.append(path[:])
                return 
            for i in range(start,n):
                path.append(i+1)
                backtrack(path,i+1)
                path.pop()
        backtrack([],0)
        return ans
        
            

        