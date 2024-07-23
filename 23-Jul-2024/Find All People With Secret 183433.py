# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parent={i:i for i in range(n)}
        rank={i:1 for i in range(n)}
        def find(x):
            if x ==parent[x]:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union( x, y):
            val_x=find(x)
            val_y=find(y)
            if val_x!=val_y:
                if rank[val_x]>rank[val_y]:
                    parent[val_y]=val_x
                elif rank[val_x]<rank[val_y]:
                    parent[val_x]=val_y   
                else:
                    parent[val_y]=val_x
                    rank[val_x]+=1
        parent[firstPerson]=0
        rank[0]+=1
        meetings.sort(key=lambda x:x[2])
        ptr=0
        while  ptr<len(meetings):
            cur_time=meetings[ptr][2]
            temp=[]
            while ptr<len(meetings) and cur_time==meetings[ptr][2]:
                x=meetings[ptr][0]
                y=meetings[ptr][1]
                parent[max(find(x),find(y))]=parent[min(find(x),find(y))]
                temp.extend([x,y])
                ptr+=1
            for i in temp:
                if find(i)!=0:
                    parent[i]=i

        res=[]
        for i in parent:
            find(i)
        for i in parent:
            if parent[i]==0:
                res.append(i)
        return res
        
        