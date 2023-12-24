class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=[]
        j=1
        for i in nums:
            if i>0:
                l.append(i)
        for i in range(len(nums)):
            if nums[i]<0 and len(nums)==2:
                l.append(nums[i])
            elif nums[i]<0:
                l.insert(j,nums[i])
                j+=2
        return l
        