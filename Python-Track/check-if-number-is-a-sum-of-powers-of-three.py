class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        l=[]
        m=n
        sum=0
        while n!=0:
            l.append(n%3)
            n=n//3
        for i in range(len(l)):
            if l[i]==0:
                continue
            sum+=(3**i)
        if sum==m:
            return True
        else:
            return False
            
        
        
        
            

        