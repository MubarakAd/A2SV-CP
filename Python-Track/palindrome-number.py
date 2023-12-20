class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        else:
            x=str(x)
            y=x[::-1]
            if x==y:
                return True
            
            else:
                return False