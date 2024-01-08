class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        count=0
        for i in nums:
            if i==0:
                count+=1
        if count==len(nums):
            n=list((set(nums)))
            n[0]=str(n[0])
            return ''.join(n)
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        return ''.join(nums)
        