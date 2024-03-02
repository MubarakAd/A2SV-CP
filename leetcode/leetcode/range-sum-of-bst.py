# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        temp=root.val
        total=[]
        def rangeSum(node,low,high,_sum):
            if node:
                if (node and node.val>=low) and (node and node.val<=high):
                    total.append(node.val)
                if not node.left and not node.right:
                    return    
                left_sum=rangeSum(node.left,low,high,total)
                right_sum=rangeSum(node.right,low,high,total)
    
                
                return sum(set(total))
            else:
                return 0
        return rangeSum(root,low,high,total)

        