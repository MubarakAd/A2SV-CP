class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:

            if i=="+":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(x)+int(y))
            elif i == "*":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(x)*int(y))
            elif i=="/":
                x=stack.pop()
                y=stack.pop()
                print(int(int(y)/int(x)))
                stack.append(int(int(y)/int(x)))
               
            elif i=="-":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y)-int(x))
            else:
                stack.append(i)
        return int(stack[0])





                
                
        