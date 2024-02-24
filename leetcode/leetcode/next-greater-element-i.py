class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict=defaultdict(int)
        stack=[]
        ans=[]
        for i in nums2:
            if len(stack)!=0:
                if stack[-1]>=i:
                    stack.append(i)
                else:
                    while stack and stack[-1]<i:
                        my_dict[stack[-1]]=i
                        stack.pop()
                    stack.append(i)
            else:
                stack.append(i)
        
        
        for i in stack:
            my_dict[i]=-1
        for i in nums1:
            ans.append(my_dict[i])
        return ans

        