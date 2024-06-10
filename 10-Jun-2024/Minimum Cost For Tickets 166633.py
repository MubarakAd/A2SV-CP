# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo={}
        def dp(ind):
            if ind>=len(days):
                return 0
            if ind not in memo:
                memo[ind]=float("inf")
                for d,c in zip([1,7,30],costs):
                    j=ind
                    while j<len(days) and days[ind]+d>days[j]:
                        j+=1
                        memo[ind]=min(memo[ind],c+dp(j))
                        
            return memo[ind]
        return dp(0)
                    
                    
