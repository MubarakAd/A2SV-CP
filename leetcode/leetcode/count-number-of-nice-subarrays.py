class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        my_dict=defaultdict(int)
        my_dict[0]=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        _sum=0
        count=0
        print(nums)
        for i in range(len(nums)):
            _sum+=nums[i]
            nums[i]=_sum
            my_dict[nums[i]]+=1
            if nums[i]-k in my_dict:
                count+=my_dict[nums[i]-k]
        print(nums)
        return count

