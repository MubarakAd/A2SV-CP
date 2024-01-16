class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=Counter(p)
        left=0
        right=len(p)
        window=Counter(s[:right])
        l=[]
        while right<len(s):
            if target==window:
                l.append(left)
            window[s[left]]-=1
            
            window[s[right]]+=1
            left+=1
            right+=1
        if target==window:
                l.append(left)
        return l
        



        