class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        print(path)
        for i in range(len(path)):
            if path[i]=="."or path[i]=='':
                continue
            elif stack and path[i]=="..":
                stack.pop()
                print(stack)
            elif path[i]=="..":
                continue
            else:
                stack.append(path[i])
            
            
        
        return "/"+'/'.join(stack)




        