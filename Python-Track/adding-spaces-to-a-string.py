class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j=0
        a=""
        for i in spaces:
            a+=s[j:i]+" "
            j=i
        a+=s[j:]
            
            
        return a