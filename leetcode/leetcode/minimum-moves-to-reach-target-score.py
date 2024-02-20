class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        num_moves=0
        while target!=1:
            if maxDoubles!=0:
                num_moves+=(target%2)+1
                target=target//2
                maxDoubles-=1
            else:
                num_moves+=(target-1)
                break
        return num_moves


        