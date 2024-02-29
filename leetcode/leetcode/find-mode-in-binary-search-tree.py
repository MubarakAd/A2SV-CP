# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        my_dict=defaultdict(int)
        ans=[]
        freq_=0
        def mode(node):
            if node is None:
                return
            my_dict[node.val] += 1
            mode(node.left)
            mode(node.right)
        mode(root)
        print(my_dict)
        for i in my_dict:
            freq_=max(freq_,my_dict[i])
        for i in my_dict:
            if my_dict[i]==freq_:
                ans.append(i)
        return ans
       
       
        
       

       

            
        