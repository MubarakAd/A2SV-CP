# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def helper(node,Total):
            if node:
                Total=Total*10+node.val
                if not node.left and not node.right:
                    return Total
                
                left_sum=helper(node.left,Total)
                right_sum=helper(node.right,Total)
                return left_sum+right_sum
            else:
                    return 0 
       
        return helper(root,0)

        