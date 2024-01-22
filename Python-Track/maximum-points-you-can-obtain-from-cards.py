class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        all_sum=sum(cardPoints)
        end_range=len(cardPoints)-k
        if end_range==0:
            return all_sum
        part_sum=0
        for i in range(end_range):
            part_sum+=cardPoints[i]
        k_sum=all_sum-part_sum
        left=0
        right=end_range
        maxx=k_sum
        while right<len(cardPoints):
            part_sum=part_sum-cardPoints[left]+cardPoints[right]
            k_sum=all_sum-part_sum
            left+=1
            right+=1
            maxx=max(maxx,k_sum)
        return maxx


        