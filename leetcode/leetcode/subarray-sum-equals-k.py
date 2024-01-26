class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict=defaultdict(int)
        my_dict[0]+=1
        prefix_sum=[0]*(len(nums))
        _sum=0
        count=0
        for i in range(len(nums)):
            _sum+=nums[i]
            prefix_sum[i]=_sum
            if prefix_sum[i]-k in my_dict:
                count+=(my_dict[prefix_sum[i]-k])
            my_dict[prefix_sum[i]]+=1
        
       
            
        return count

        print(prefix_sum)
        print(my_dict)



        