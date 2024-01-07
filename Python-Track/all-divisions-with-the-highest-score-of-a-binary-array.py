class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        my_set=set()
        my_dic={}
        ans=[]
        ze_l=[]
        on_l=[0]*(len(nums)+1)
        ze_count=0
        ze_l.append(ze_count)
        for i in range(len(nums)):
                    if nums[i]==0:
                        ze_count+=1
                    ze_l.append(ze_count)
        on_count=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==1:
                on_count+=1
            on_l[i]=on_count
        for i in range(len(on_l)):
            my_dic[i]=on_l[i]+ze_l[i]
        my_dic=dict(sorted(my_dic.items(), reverse=True ,key=lambda item: item[1]))
        count=0
        for i in my_dic:
            if count==1:
                if my_dic[i] in my_set:
                    ans.append(i)
                    my_set.add(my_dic[i])
                else:
                    break
            else:
                ans.append(i)
                my_set.add(my_dic[i])
                count=1
        return ans

    

    
            
