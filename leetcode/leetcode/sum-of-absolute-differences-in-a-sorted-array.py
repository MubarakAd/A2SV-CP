class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref=[0]*len(nums)
        _sum=0
        for i in range(len(nums)):
            _sum+=nums[i]
            pref[i]=_sum
        m=[]
        lenn=len(nums)-1
        for i in range(len(pref)):
            val=abs((_sum-pref[i])-(nums[i]*(lenn-i)))+abs((nums[i]*(i+1))-pref[i])
            m.append(val)
        return m

