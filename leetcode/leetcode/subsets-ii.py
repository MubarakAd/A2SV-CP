class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        store=set()
        def subset2(temp,indx):
            if len(temp)<=len(nums):
                if tuple(temp) not in store:
                    res.append(temp[:])
                store.add(tuple(temp))
            else:
                return 
            for i in range(indx,len(nums)):
                temp.append(nums[i])
                subset2(temp,i+1)
                temp.pop()
        subset2([],0)
        return res

        