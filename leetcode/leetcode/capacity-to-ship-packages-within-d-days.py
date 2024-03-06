class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       left,right,best=max(weights),sum(weights),-1
       while left<=right:
           mid=(right+left)//2
           calculated,counter=0,1
           for i in range(len(weights)):
               calculated+=weights[i]
               if calculated>mid:
                   calculated=weights[i]
                   counter+=1
           if counter>days:
                left = mid + 1
           else:
                right = mid - 1
                best = mid
       return best

                
                   
