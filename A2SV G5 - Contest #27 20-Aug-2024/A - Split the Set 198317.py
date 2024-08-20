# Problem: A - Split the Set - https://codeforces.com/gym/538762/problem/A

t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even+=1
        else:
            odd+=1
    # print(even,odd)
    if even==odd and (even%n==0 and odd%n==0):
        print("Yes")
    else:
        print("No")
            
