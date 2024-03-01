# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans=[]
        _min=float("inf")
        maxx=float("-inf")
        def helper(node,_min,maxx):
            if node:
                _min=min(_min,node.val)
                maxx=max(maxx,node.val)
                
                if  not node.left and not node.right:
                    ans.append(abs((maxx)-(_min)))
                    return 
                left=helper(node.left,_min,maxx)
                right=helper(node.right,_min,maxx)
                return
            else:
                return 0
        helper(root,_min,maxx)
        
        return max(ans)

