class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        import math
        ms=[]
        m=Counter(nums)
        for i in m.keys():
             if m[i]>math.floor(len(nums)/3):
                ms.append(i)
        return ms
        