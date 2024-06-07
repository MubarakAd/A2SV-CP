# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        my_dict=Counter(nums)
        ptr=0
        count=0
        nums.sort()
        while ptr<len(nums):
            x=k-nums[ptr]
            if nums[ptr] in my_dict:
                if x==nums[ptr] and x in my_dict:
                    if my_dict[x]>=2:
                        count+=1
                        my_dict[x]-=2
                        if my_dict[x]==0:
                            del my_dict[x]
                elif x in my_dict:
                    count+=1
                    my_dict[x]-=1
                    my_dict[nums[ptr]]-=1
                
                    if my_dict[x]==0:
                        del my_dict[x]
                    if my_dict[nums[ptr]]==0:
                        del my_dict[nums[ptr]]
            ptr+=1
        return count
                

