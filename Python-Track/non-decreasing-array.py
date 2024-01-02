class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        left=0
        right=1
        flag=False
        while right<=len(nums)-1:
            if flag and nums[left]>nums[right]:
                return False
            else:
                if nums[left]>nums[right]:
                    if right!=len(nums)-1 and nums[left]>nums[right+1]:
                        if left!=0 and nums[right]>=nums[left-1]:
                            nums[left]=nums[right]
                        elif left!=0 and nums[right]<nums[left-1]:
                            return False
                        else:
                            nums[left]=nums[right]
                    else:
                        nums[right]=nums[left]
                    flag=True
                    


                else:
                    right+=1
                    left+=1
        print(nums)
        return True
        
                
            
        