class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<=k:
            s=s[::-1]
            return s
        else:
            left=0
            right=k
            s=list(s)
            while right<=len(s)-1:
                if left==0:
                     s[left:right]=s[right-1::-1]
                     left+=2*k
                     right+=2*k
                else:
                    s[left:right]=s[right-1:left-1:-1]
                    left+=2*k
                    right+=2*k
            if right>len(s)-1 and left<len(s)-1:
                s[left:]=s[len(s)-1:left-1:-1]
            return ''.join(s)


