class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum=[0]*len(nums)
        pos_sum=[0]*len(nums)
        ans=[]
        _sum=1
        for i in range(len(nums)):
            _sum*=nums[i]
            pre_sum[i]=_sum
        _sum=1
        for i in range(len(nums)-1,-1,-1):
            _sum*=nums[i]
            pos_sum[i]=_sum
        for i in range(len(nums)):
            if i==0:
                ans.append(pos_sum[i+1])
            elif i ==len(nums)-1:
                ans.append(pre_sum[i-1])
            else:
                ans.append(pre_sum[i-1]*pos_sum[i+1])
        return ans
        

        