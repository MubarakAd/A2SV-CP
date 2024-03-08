class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # left=right=0
        # while right<len(temp):
        #     if right-left==k:
        #         if temp[right]<temp[left]:
        #             left+=1
        #         else:
        #            right+=1
        #     else:
        #         right+=1
            
        # return arr[left:right]
        queue=deque()
        temp=[0]*len(arr)
        for i in range(len(arr)):
            temp[i]=abs(arr[i]-x)
        left=right=0
        print(temp)
        while right<len(temp):
            if len(queue)<k:
                queue.append(right)
            elif len(queue)==k:
                if temp[right]<temp[left]:
                    queue.popleft()
                    queue.append(right)
                    if len(queue)>1:
                        queue[0]=queue[-1]-(len(queue)-1)
                    left+=1
            right+=1
        print(queue)
        return arr[queue[0]:queue[-1]+1]
            
        