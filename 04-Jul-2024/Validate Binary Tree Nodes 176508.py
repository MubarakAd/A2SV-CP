# Problem: Validate Binary Tree Nodes - https://leetcode.com/problems/validate-binary-tree-nodes/

from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        temp = {}
        for i in range(n):
            temp[i] = 1

        for i in range(n):
            if(leftChild[i]!=-1):
                graph[i].append(leftChild[i])
                if(leftChild[i] in temp):
                    del temp[leftChild[i]]
            if(rightChild[i]!=-1):
                graph[i].append(rightChild[i])
                if(rightChild[i] in temp):
                    del temp[rightChild[i]]

        if(len(temp)!=1):
            return False

        for key in temp.keys():
            root = key

        def dfs(node):
            if(node in visited):
                return False
            ans = True
            visited[node] = 1
            for child in graph[node]:
                ans = ans and dfs(child)
            return ans

        visited = {}
        ans = dfs(root)
        if(ans and len(visited)==n):
            return True
        return False