class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split(" ")
        l=[]
        maxx=0
        for i in s:
            maxx=max(maxx,len(i))
        for i in range(maxx):
            ans=""
            for j in range(len(s)):
                if i<len(s[j]):
                    ans+=s[j][i]
                else:
                    ans+=" "
            l.append(ans.rstrip())
        return l
        