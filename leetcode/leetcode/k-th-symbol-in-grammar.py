class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(k):
            if k==1:
                return 0
            dir=''
            
            if 2*int(k//2)==2*(k/2):
                dir=="r"
            else:
                dir="l"
            bit=solve(ceil(k/2))
            if bit==0:
                if dir=="l":
                    return 0
                else:
                    return 1
            else:
                if dir=="l":
                    return 1
                else:
                    return 0

        return solve(k)

        