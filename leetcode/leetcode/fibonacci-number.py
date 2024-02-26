class Solution:
    def fib(self, n: int) -> int:
        def fibb(n):
            if n==1 or n==0:
                return n
            return fibb(n-1)+fibb(n-2)
        return fibb(n)

        