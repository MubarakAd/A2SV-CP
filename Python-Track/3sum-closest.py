class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        my_dic=defaultdict(int)
        nums.sort()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                _sum=0
                _sum=nums[i]+nums[left]+nums[right]
                my_dic[_sum]=abs(_sum-target)
                if nums[i]+nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
        my_dic=dict(sorted(my_dic.items(),key= lambda item :item[1]))
        for i in my_dic:
            return i
            

        