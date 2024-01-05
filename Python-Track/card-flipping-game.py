class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        my_set = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in my_set:
                my_set.remove(fronts[i])
        if len(my_set) == 0:
            return 0
        else:
            return my_set.pop()
        
        