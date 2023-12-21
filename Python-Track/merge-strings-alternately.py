class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
           l1=list(word1)
           l2=list(word2)
           l=[]
           n=min(len(l1),len(l2))
           for i in range(n):
                l.append(l1[i])
                l.append(l2[i])
           if i<len(l1)-1:
                l.extend(l1[i+1:])
           elif i<len(l2)-1:
                l.extend(l2[i+1:])
           return ''.join(l)
                
                
            
    
    
        