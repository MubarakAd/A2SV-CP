class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum=0
        while n>1:
            if n%2==0:
                n=n//2
                sum+=n
            else:
                sum+=((n-1)//2)
                n=(n+1)//2
        return sum
                
        