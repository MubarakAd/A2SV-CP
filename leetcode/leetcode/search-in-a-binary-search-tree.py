# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        def search(node):
            if node and node.val==val:
                return node
            if node and node.val>val:
                return search(node.left)
            elif node and node.val<val:
                return  search(node.right)
        
        return search(root)
        