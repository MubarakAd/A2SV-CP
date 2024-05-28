# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq
my_heap=[]
ans=[]
t=int(input())
for i in range(t):
    ipt=[i for i in input().split()]
    if ipt[0]=="insert":
        heapq.heappush(my_heap,int(ipt[1]))
        ans.append(("insert",int(ipt[1])))
    elif ipt[0]=="getMin":
        if len(my_heap)==0:
            heapq.heappush(my_heap,int(ipt[1]))
            ans.append(("insert",int(ipt[1])))
            ans.append(("getMin",my_heap[0]))
            
        elif my_heap[0]!=int(ipt[1]):
            while len(my_heap)>0 and my_heap[0]<int(ipt[1]):
                heapq.heappop(my_heap)
                ans.append(("removeMin",float("inf")))
            if not my_heap or my_heap[0]!=int(ipt[1]):
                heapq.heappush(my_heap,int(ipt[1]))
                ans.append(("insert",int(ipt[1])))
            ans.append(("getMin",int(ipt[1])))
        elif my_heap[0]==int(ipt[1]):
            ans.append(("getMin",int(ipt[1])))
    elif ipt[0]=="removeMin":
        if len(my_heap)>0:
            heapq.heappop(my_heap)
            ans.append(("removeMin",float("inf")))
        else:
            heapq.heappush(my_heap,0)
            ans.append(("insert",0))
            heapq.heappop(my_heap)
            ans.append(("removeMin",float("inf")))
n=len(ans)
print(n)
for i ,j in ans:
    if j!=float("inf"):
        print(i,j)
    else:
        print(i)
        
        
    
        
    