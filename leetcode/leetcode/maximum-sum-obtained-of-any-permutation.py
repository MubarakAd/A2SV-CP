class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref=[0]*(len(nums)+1)
        for i,j in requests:
            pref[i]+=1
            pref[j+1]-=1
        _sum=0
        for i in range(len(pref)):
            _sum+=pref[i]
            pref[i]=_sum
        nums.sort(reverse=True)
        pref.sort(reverse=True)
        max_sum=0
        for i in range(len(nums)):
            max_sum+=(nums[i]*pref[i])
        return max_sum % (10**9 + 7)
