class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        left=0
        right=1
        while left!=len(nums)-1:
            if  nums[left]+nums[right]==target:
                l.append(left)
                l.append(right)
                return l
                break
            elif right==len(nums)-1:
                left+=1
                right=left+1
            else:
                right+=1

            