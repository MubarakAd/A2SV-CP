class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        i=0
        while n<=len(nums)-1:
            l.append(nums[i])
            l.append(nums[n])
            i+=1
            n+=1
        return l
            
        