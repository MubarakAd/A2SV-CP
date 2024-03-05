class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def perm(temp,ind):
            nonlocal ans
            if len(temp)<=len(nums):
                ans.append(temp[:]) 
            for i in range(ind,len(nums)):
                temp.append(nums[i])
                perm(temp,i+1)
                temp.pop()
        perm([],0)
        return ans
        