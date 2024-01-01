class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        ans=[0]*len(nums)
        my_dic={nums[i]:i for i in range(len(nums))}
        for x,y in operations:
            nums[my_dic[x]]=y
            i=my_dic[x]
            my_dic[y]=i
            del my_dic[x]
        for i in my_dic:
            ans[my_dic[i]]=i
        return ans