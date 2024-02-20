class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr_max =nums[0]
        summ = nums[0]
        for i in range(1,len(nums)):
            summ += nums[i]
            if nums[i] > curr_max:
                curr_max = max(curr_max,math.ceil(summ/(i+1)))
        return curr_max    