class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        a=[]
        count=0
        _set=set(arr2)
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                           if arr1[j]==arr2[i]:
                                l.append(arr1[j])
                           elif arr1[j] not in _set and count==0:
                                a.append(arr1[j])
            count=1
        a.sort()
        l.extend(a)
        return l
                                
                           
            
        