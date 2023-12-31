class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        left=0
        right=1
        count=0
        maxx=float("-inf")
        flag=False
        if len(nums)==1:
            return 1
        elif len(nums)==0:
            return 0
        else:
            while right<=len(nums)-1:
                if nums[left]+1==nums[right]:
                    count+=1
                    right+=1
                    left+=1
                else:
                    maxx=max(maxx,count+1)
                    count=0
                    right+=1
                    left+=1
                    flag=True
        if flag:
            return max(maxx,count+1)
        else:
            return count+1