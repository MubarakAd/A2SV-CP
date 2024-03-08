class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def grammer(k):
            if k==1:
                return 0
            dir=''
            if 2*(k/2)==2*(k//2):
                dir="r"
            else:
                dir="l"
            ans=grammer(ceil(k/2))
            if ans==0:
                if dir=='l':
                    return 0
                else:
                    return 1
            else:
                if dir=="l":
                    return 1
                else:
                    return 0
        

        return grammer(k)

        