class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        my_dict=defaultdict(list)
        lenn=len(costs)
        count=0
        total=0
        costs.sort(key=lambda x:x[0]-x[1])
        for costA,costB in costs:
            if count<lenn//2:
                total+=costA
            else:
                total+=costB
            count+=1
        print(costs)
        return total
        