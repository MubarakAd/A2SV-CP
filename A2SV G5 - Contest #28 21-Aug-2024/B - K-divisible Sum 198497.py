# Problem: B - K-divisible Sum - https://codeforces.com/gym/540354/problem/B

t=int(input())
for i in range(t):
    n,k= [int(i) for i in input().split()]
    _sum = (n + k - 1) // k
    k *= _sum
    res = (k + n - 1) // n
    print(res)
