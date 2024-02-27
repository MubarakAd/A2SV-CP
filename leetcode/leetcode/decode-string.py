class Solution:
    def decodeString(self, s: str) -> str: 
        stack=[]
       
        for i in range(len(s)):
            if len(stack)!=0:
                if s[i]!="]":
                    stack.append(s[i])
                else:
                    num=[]
                    alph=[]
                    while stack and not stack[-1].isdigit():
                        if stack[-1].isalpha():
                            x=stack.pop()
                            alph.append(x)
                        else:
                             stack.pop()
                    while stack and stack[-1].isdigit():
                        y=stack.pop()
                        num.append(y)
                    num=num[::-1]
                    alph=alph[::-1]
                    mult="".join(num) 
                    concat_=''.join(alph)
                    concat_=concat_*int(mult)
                    print(concat_) 
                    print(mult)
                    stack.append(concat_) 
            else:
               stack.append(s[i]) 
        return ''.join(stack)  
        