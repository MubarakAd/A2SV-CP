# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        used=[False]*len(nums)
        target=sum(nums)//k
        memo={}
        nums.sort(reverse=True)
        def dp(ind,k,sum_):
            if k==0:
                return True
            if sum_==target:
                return dp(0,k-1,0)
            if (tuple(used),k,sum_) not in memo:
                for j in range(ind,len(nums)):
                    if used[j] or sum_+nums[j]>target:
                        continue
                    used[j]=True
                    if dp(j+1,k,sum_+nums[j]):
                        memo[(tuple(used),k,sum_)]=True
                        return True
                    used[j]=False
                memo[(tuple(used),k,sum_)]=False
                return False
            return memo[(tuple(used),k,sum_)]     
        return dp(0,k,0)
            
    
        

     
    

    
        
    
                    
                    
                    
                
    