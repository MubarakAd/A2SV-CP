class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
      my_dic=Counter(nums)
      my_list=list(set(nums))
      my_list.sort()
      ans=0
      for i in range(len(my_list)-1,0,-1):
          ans+=my_dic[my_list[i]]
          my_dic[my_list[i-1]]+=my_dic[my_list[i]]
      return ans
          
                
            
        