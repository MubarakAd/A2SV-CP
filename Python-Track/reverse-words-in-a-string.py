class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        l=[]
        for i in range(len(s)-1,-1,-1):
            if s[i]!="":
                l.append(s[i])
        return ' '.join(l)
        