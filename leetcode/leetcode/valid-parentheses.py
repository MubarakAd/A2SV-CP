class Solution:
    def isValid(self, s: str) -> bool:
       store=[]
       if len(s)==1:
           return False
       for i in s:
           if i=="[" or i=="{" or i=="(":
               store .append(i)
           elif i=="]":
               if len(store)>=1:
                    if store[-1]=="[":
                        store.pop()
                    else:
                        return False
               else:
                   return False
           elif i=="}":
               if len(store)>=1:
                    if store[-1]=="{":
                        store.pop()
                    else:
                            return 
                            False
               else:
                   return False
           elif i==")":
               if len(store)>=1:
                    if store[-1]=="(":
                        store.pop()
                    else:
                        return False
               else:
                   return False
       if len(store)==0:
            return True
       else:
            return False

        
                