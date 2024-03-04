class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.max_total=float("inf")
        def func(ditribution,ind):
            if ind==len(cookies):
                self.max_total=min(self.max_total,max(distribution))
                return 
            for i in range(k):
                distribution[i]+=cookies[ind]
                if distribution[i]<=self.max_total:
                    func(distribution,ind+1)
                distribution[i]-=cookies[ind]
        distribution=[0]*k
        func(distribution,0)
        return self.max_total