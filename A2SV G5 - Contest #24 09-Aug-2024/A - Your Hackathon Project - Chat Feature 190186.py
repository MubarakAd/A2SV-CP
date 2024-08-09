# Problem: A - Your Hackathon Project - Chat Feature - https://codeforces.com/gym/534160/problem/A

import sys
from collections import Counter
def I(): return int(sys.stdin.readline().strip())
def ILT(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SLT(): return sys.stdin.readline().strip().split()
def DIG(): return [int(i) for i in (list(sys.stdin.readline().strip()))]
def CHAR(): return list(sys.stdin.readline().strip())
t=I()
for i in range(t):
    n=I()
    s=S()
    cnt=0
    for i in s:
        if i==")":
            cnt+=1
        else:
            cnt=0
    check=len(s)-cnt
    if cnt>check:
        print("YES")
    else:
        print("NO")
    