# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref=[0]*len(nums)
        my_dict=defaultdict(int)
        my_dict[0]+=1
        _sum=0
        count=0
        for i in range(len(nums)):
            _sum+=nums[i]
            pref[i]=_sum
            if pref[i]%k in my_dict:
                count+=(my_dict[pref[i]%k])
            my_dict[pref[i]%k]+=1  
        return count


        