class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack=[]
        # ans=[]
        # for i in range(1,len(temperatures)):
        #     if len(stack)!=0:
        #         if temperatures[stack[-1]]<temperatures[i]:
        #             while stack and temperatures[stack[-1]]<temperatures[i]:
        #                     x=stack.pop()
        #                     ans.append(i-x)
        #             stack.append(i)   
        #         else:
        #             stack.append(i)
        #     else:
        #         stack.append(i)
        # print(stack)
        
        # return ans
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stack)!=0:
                if temperatures[stack[-1]]>temperatures[i]:
                    stack.append(i)
                else:
                    while stack and temperatures[stack[-1]]<temperatures[i]:
                        x=stack.pop()
                        ans[x]=i-x
                    stack.append(i)
            else:
                stack.append(i)
        return ans




        