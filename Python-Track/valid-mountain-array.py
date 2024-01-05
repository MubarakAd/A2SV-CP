class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag=False
        if len(arr)<=2 or arr[0]==max(arr) or arr[len(arr)-1]==max(arr):
                return False
        else:
    
                for i in range(len(arr)-1):
                    if arr[i+1]>arr[i] and not flag:
                        count=1
                    elif arr[i]>arr[i+1]:
                        flag=True
                    else:
                        return False
        return True
                    
                
        