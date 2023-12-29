class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans=[]
        l=[]
        for i in range(left,right+1):
            l.append(i)
        for i in  range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                if j in l:
                    ans.append(j)
        my_list=list(set(ans))
        my_list.sort()
        if my_list==l:
            return True
        else:
            return False  