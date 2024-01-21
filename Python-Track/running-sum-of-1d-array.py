class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _sumList=[]
        _sum=0
        for i in nums:
            _sumList.append(_sum+i)
            _sum+=i
        return _sumList