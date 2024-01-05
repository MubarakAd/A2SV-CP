class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=''
        if len(s)==0:
            return True
        else:
            for i in s:
                if i.isalnum():
                    ans+=i
        ans=ans.lower()
        print(ans)
        if ans==ans[::-1]:
            return True
        else:
            return False
        
        