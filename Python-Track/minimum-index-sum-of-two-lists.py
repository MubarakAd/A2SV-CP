class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minn=float('inf')
        l=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                minn=min(minn,i+list2.index(list1[i]))
        for i in range(len(list1)):
            if list1[i] in list2 and i+list2.index(list1[i])==minn:
                l.append(list1[i])
        return l