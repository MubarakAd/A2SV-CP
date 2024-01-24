class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum=[0]*len(nums)
        pre_sum=0
        for i in range(len(nums)):
            pre_sum+=nums[i]
            prefix_sum[i]=pre_sum
        postfix_sum=[0]*len(nums)
        pos_sum=0
        for i in  range(len(nums)-1,-1,-1):
            pos_sum+=nums[i]
            postfix_sum[i]=pos_sum
        for i in range(len(nums)):
            if prefix_sum[i]==postfix_sum[i]:
                return i
        return -1


        