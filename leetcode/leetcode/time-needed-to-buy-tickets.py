class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken=0
        temp=tickets[k]
        for i in range(k):
            if tickets[i]>temp:
                time_taken+=temp
            else:
                time_taken+=tickets[i]
        for i in range(k+1,len(tickets)):
            if tickets[i]>=temp:
                time_taken+=(temp-1)
            else:
                time_taken+=tickets[i]
        return time_taken+temp


        