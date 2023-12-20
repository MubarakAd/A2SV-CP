class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        l=[]
        m=num
        num=num//3
        sum=num+(num+1)+(num-1)
        if sum==m:
            l.append(num-1)
            l.append(num)
            l.append(num+1)
            return l
        else:
            return l
            
        
                
        