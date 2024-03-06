class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)
            print(perms)
            for i in perms:
                i.append(n)
            res.extend(perms)
            nums.append(n)
        return res
        
        # ans=[]
        # def perm(temp,ind):
        #     if len(temp)==len(nums):
        #         ans.append(temp[:])
             
        #     for i in range(ind,len(nums)):
        #         temp.append(nums[i])
        #         perm(temp,ind+1)
        #         temp.pop()
        # perm([],0)
        # return ans

            

        