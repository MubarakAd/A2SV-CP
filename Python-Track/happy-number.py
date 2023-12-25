class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        nums=[]
        while int(n)!=1 and n not in nums:
            sum=0
            for i in n:
                sum+=int(i)**2
            nums.append(n)
            n=str(sum)
        if  int(n)==1:
            return True
        else:
            return False
