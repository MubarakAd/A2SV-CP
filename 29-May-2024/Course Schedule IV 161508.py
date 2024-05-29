# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for pre,course in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        queue=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        res=defaultdict(set)
        while queue:
            node=queue.popleft()
            for neigh in graph[node]:
                indegree[neigh]-=1
                res[neigh].add(node)
                for i in res[node]:
                    res[neigh].add(i)
                if indegree[neigh]==0:
                    queue.append(neigh)
        ans=[False]*len(queries)
        ind=0
        for u,v in queries:
            if u in res[v]:
                ans[ind]=True
            ind+=1
        return ans

       

        