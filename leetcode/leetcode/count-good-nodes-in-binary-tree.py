# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def helper(node,max_):
            if node is None:
                return
            if node.val>=max_:
                self.count+=1
                max_=max(node.val,max_)
            helper(node.right,max_)
            helper(node.left,max_)
        helper(root,float("-inf"))
        return self.count
        