class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans=[]
        for right in firstList:
            
            for left in secondList:
                l=[]
                l.append(max(left[0],right[0]))
                if min(left[1],right[1])>=l[0]:
                    l.append(min(left[1],right[1]))
                    ans.append(l)
                    
                else:
                    continue
        return ans


        