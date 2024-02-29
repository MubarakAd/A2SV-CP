# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def inorder(node,ans):
            if node:
                # first recur on left child
                inorder(node.left,ans)
                # then add the data of node
                ans.append(node.val),
                # now recur on right child
                inorder(node.right,ans)
            else:
                return node
        inorder(root,ans)
        for i in range(len(ans)-1):
            if ans[i]>=ans[i+1]:
                return False
        return True
            
      
        