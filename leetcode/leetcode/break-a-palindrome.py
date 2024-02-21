class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lst=list(palindrome)
        if len(palindrome)==1:
            return ""
        for i in range(len(lst)):
            if i==len(lst)-1:
                lst[i]="b"
            elif lst[i]!="a" and lst.count(lst[i])>1:
                lst[i]="a"
                break
        return ''.join(lst)