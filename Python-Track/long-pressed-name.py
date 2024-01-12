class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left=0
        right=0
        if typed[left]!=name[right]:
            return False
        while left<len(typed) and right<len(name):
            if name[right]==typed[left]:
                left+=1
                right+=1
            elif name[right]!=typed[left]:
                left+=1
                if left<len(typed):
                    if name[right]!=typed[left] and typed[left-1]!=typed[left]:
                        return False
        if right==len(name) and left==len(typed):
            return True
        elif right==len(name) and left<len(typed) and set(typed[left:])==set(name[right-1]):
            return True
        else:
           return False
        
        
        
        

        