class Solution:
    def minimumSteps(self, s: str) -> int:
        left=0
        right=len(s)-1
        count=0
        s=list(s)
        while left<right:
            if s[right]=="0" and s[left]=="1":
                count+=(right-left)
                left+=1
                right-=1
            elif s[right]=="1" and s[left]=="1":
                right-=1
            elif  s[right]=="0" and s[left]=="0":
                left+=1
            else:
                left+=1
                right-=1

               
        return count
        
        