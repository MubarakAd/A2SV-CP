# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums==[]:
            return None
        max_=max(nums)
        node=TreeNode(max_)
        node.left=self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
        node.right=self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
        return node
        