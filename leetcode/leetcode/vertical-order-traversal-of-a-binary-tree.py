# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict=defaultdict(list)
        res=[]

        def v_traversal(node,row,col):
            if node:
                v_traversal(node.left,row+1,col-1)
                my_dict[col].append((row,node.val))
                v_traversal(node.right,row+1,col+1)
            else:
                return
        v_traversal(root,0,0)
        res=[0]*len(my_dict)
        for i in my_dict:
            my_dict[i].sort()
        min_=float("inf")
        for  i in my_dict:
            min_=min(min_,i)
        min_=-min_
        for i in my_dict:
            temp=[]
            for j in my_dict[i]:
                temp.append(j[1])
            res[min_+i]=temp
        return res




        