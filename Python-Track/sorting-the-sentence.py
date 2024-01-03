class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        l=[0]*len(s)
        for i in s:
            l[int(i[len(i)-1])-1]=i[0:len(i)-1]
        return ' '.join(l)
