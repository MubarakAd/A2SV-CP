class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pref=[0]*len(s)
        _sum=0
        for i in range(len(pref)):
            if s[i]=="|":
                _sum+=1
            pref[i]=_sum
        ans=[]
        for i,j in queries:
            left=right=0
            if s[i]=="|":
                left=i
            else:
                left=min(bisect_right(pref,pref[i]),len(s)-1)
            if s[j]=="|":
                right=j
            else:
                right=max(bisect_left(pref,pref[j]),0)
            res=right-left-(pref[right]-pref[left])
            if res<0:
                ans.append(0)
            else:
                ans.append(res)
            # ans.append(max(0,res))
        return ans