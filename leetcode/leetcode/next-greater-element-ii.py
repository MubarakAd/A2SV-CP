class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1]*len(nums)
        lenn=len(nums)
        nums=2*nums
        for i in range(len(nums)):
            if len(stack)!=0:
                if nums[stack[-1]]>nums[i%lenn]:
                    stack.append(i%lenn)
                else:
                    while stack and  nums[stack[-1]]<nums[i%lenn]:
                        ans[stack[-1]]=nums[i%lenn]
                        stack.pop()
                    stack.append(i%lenn)
            else:
                stack.append(i%lenn)

        return ans
        