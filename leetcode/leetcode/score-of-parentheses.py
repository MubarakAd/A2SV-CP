class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
            elif i==")":
                if stack[-1]=="(":
                    stack.pop()
                    if stack:
                        if stack[-1]=="(":
                            stack.append(1)
                        else: 
                            stack[-1]=stack[-1]+1
                    else:
                        stack.append(1)
                else:
                    x=stack.pop()
                    while stack[-1]!="(":
                        stack.pop()
                    stack.pop()
                    if stack:
                        if stack[-1]=="(":
                            stack.append(x*2)
                        else:
                            stack[-1]=stack[-1]+(x*2)
                    else:
                        stack.append(x*2)
                        
        return stack[0]
                    



        