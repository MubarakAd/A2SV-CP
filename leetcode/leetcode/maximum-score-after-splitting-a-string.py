class Solution:
    def maxScore(self, s: str) -> int:
        left_fix=[0]*len(s)
        right_fix=[0]*len(s)
        l_sum=0
        for i in range(len(s)):
            if s[i]=="0":
                l_sum+=1
            left_fix[i]=l_sum
        r_sum=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="1":
                r_sum+=1
            right_fix[i]=r_sum
        maxx=float("-inf")
        for i in range(len(s)-1):
           maxx=max(maxx,left_fix[i]+right_fix[i+1])
        return maxx




        