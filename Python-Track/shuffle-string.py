class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[0]*len(s)
        j=0
        for i in indices:
            l[i]=s[j]
            j+=1
        return ''.join(l)