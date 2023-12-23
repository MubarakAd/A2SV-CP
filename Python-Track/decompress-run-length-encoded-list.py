class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        l=[]
        while right<=len(nums)-1:
            itr = nums[left]
            for i in range(itr):

                l.append(nums[right])
            left+=2
            right+=2
        return l