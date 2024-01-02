class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        l=[]
        count=0
        for i in range(len(strs[0])):
            ans=""
            for j in range(len(strs)):
                ans+=strs[j][i]
            l.append(ans)
        print(l)
        for i in range(len(l)):
            if list(l[i])!=sorted(l[i]):
                 count+=1
            
        return count
                
        