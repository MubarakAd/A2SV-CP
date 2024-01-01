class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l_lost=[]
        not_lost=set()
        lost=[]
        lost_1=set()
        ans=[]
        for i in range(len(matches)):
            lost.append(matches[i][1])
        l_lost=lost
        lost=set(lost)
        for i in range(len(matches)):
            if matches[i][0] not in lost:
                not_lost.add(matches[i][0])
        my_dic=Counter(l_lost)
        for i in my_dic:
            if my_dic[i]==1:
                lost_1.add(i)
        lost_1=list(lost_1)
        lost_1.sort()
        not_lost=list(not_lost)
        not_lost.sort()
        return [not_lost,lost_1]
