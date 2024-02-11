class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l=len(arr)
        result=[]
        for indx in range(l):
            max_=max(arr[:l-indx])
            max_indx=arr.index(max_)+1
            arr[:max_indx]=reversed(arr[:max_indx])
            result.append(max_indx)
            arr[:l-indx]=reversed(arr[:l-indx])
            result.append(l-indx)
        return result