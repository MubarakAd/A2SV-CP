class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left=0
        right=1
        l=[]
        while right<=len(num)-1:
            if num[left]==num[right] and right<len(num)-1:
                right+=1
                if num[left]==num[right]:
                    l.append(num[left:right+1])
                    left=right+1
                    right=left+1
                else:
                    left=right
                    right=left+1
            else:
                left+=1
                right+=1
        if len(l)!=0:
             return str(max(l))
        else:
            return ""
            
                        
       
        