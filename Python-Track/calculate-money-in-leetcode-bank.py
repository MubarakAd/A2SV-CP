class Solution:
    def totalMoney(self, n: int) -> int:
        add=1
        sum=0
        j=1
        for i in range(1,n+1):
            if (i-1)%7==0 and i!=1:
                j+=1
                add=j
            sum+=add
            add+=1
        return sum
                
            
            
        