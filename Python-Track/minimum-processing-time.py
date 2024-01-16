class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        end=4
        maxx=float("-inf")
        for i in range(len( processorTime)):
            maxx=max(maxx,processorTime[i]+tasks[end-1])
            end+=4
        return maxx
           
           



        