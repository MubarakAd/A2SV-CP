class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict=defaultdict(int)
        my_dict[0]+=1
        count=0
        _sum=0
        for i in range(len(nums)):
            _sum+=nums[i]
            nums[i]=_sum
            if nums[i]-goal in my_dict:
                count+=my_dict[nums[i]-goal]
            my_dict[nums[i]]+=1
        return count
            