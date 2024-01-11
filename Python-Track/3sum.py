class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        st=set()
        for i in  range(len(nums)-2):
            right=len(nums)-1
            left=i+1
            -4,-1,-1,0,1,2
            while left<right:
                l=[]
                if nums[i]+nums[left]+nums[right]==0:
                    t=(nums[i],nums[left],nums[right])
                    st.add(t)
                    left+=1
                elif  nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    left+=1
        for i in st:
            ans.append(list(i))
        return ans 
