class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict=Counter(s)
        palindrome_len=0
        max_odd=0
        for i in my_dict:
            if my_dict[i]%2==0:
                palindrome_len+=my_dict[i]
            else:
                max_odd=max(max_odd,my_dict[i])
        print(my_dict)
        palindrome_len+=max_odd
        flag=False
        for i in my_dict:
            if my_dict[i]%2!=0:
                if my_dict[i]==max_odd and not flag:
                    flag=True
                elif my_dict[i]==max_odd and flag:
                    palindrome_len+=(my_dict[i]-1)
                else:
                    palindrome_len+=(my_dict[i]-1)      
        return palindrome_len
        