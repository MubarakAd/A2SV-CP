class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        left=0
        right=1
        bag=[]
        while right<len(weights):
            addd=weights[left]+weights[right]
            bag.append(addd)
            left+=1
            right+=1
        left=0
        right=len(weights)-1
        bag.sort()
        left_sum=sum(bag[0:left+(k-1)])
        right_sum=sum(bag[right-(k-1):right+1])
        return right_sum-left_sum