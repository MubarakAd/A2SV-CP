class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if i=="../" and len(stack)!=0:
                stack.pop()
            elif i=="./":
                continue
            else:
                if i!="../":
                    stack.append(i)
        print(stack)
        return len(stack)
            


        