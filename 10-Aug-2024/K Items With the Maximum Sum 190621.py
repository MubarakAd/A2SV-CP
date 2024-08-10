# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        num_ones=[1]*numOnes
        num_zero=[0]*numZeros
        num_neg=[-1]*numNegOnes
        l=[]
        l.extend(num_ones)
        l.extend(num_zero)
        l.extend(num_neg)
        _sum=0
        for i in range(k):
            _sum+=l[i]
        return _sum
        