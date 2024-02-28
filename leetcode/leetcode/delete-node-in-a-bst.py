# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        else:
            if root.val>key:
                root.left=self.deleteNode(root.left,key)
            elif root.val<key:
                root.right=self.deleteNode(root.right,key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    max_value=root.left
                    while max_value.right:
                        max_value=max_value.right
                    root.val=max_value.val
                    root.left=self.deleteNode(root.left,max_value.val)
        return root
        