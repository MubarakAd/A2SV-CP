class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_lis=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                my_lis[i+j].append(mat[i][j])
        ans=[]
        for i in my_lis:
            if i%2==0:
                ans.extend(my_lis[i][::-1])
            else:
                ans.extend(my_lis[i])
        return ans
        