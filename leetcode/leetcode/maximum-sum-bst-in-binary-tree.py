# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkLr(self, node, left_max, right_min):
        if left_max >= node.val or right_min <= node.val:
            return False
        return True
    def dfs(self, node):
        if not node:
            return [0, float("inf"), float("-inf")]
        lsm, lmin, lmax = self.dfs(node.left)
        rsm, rmin, rmax = self.dfs(node.right)
        if self.checkLr(node, lmax, rmin) and lsm != "inv" and rsm != "inv":
            curr_min = min(lmin, rmin, node.val)
            curr_max = max(rmax, lmax, node.val)
            s = lsm + rsm + node.val
            self.ans = max(self.ans, s)
            return [s, curr_min, curr_max]
        return ["inv", node.val, node.val]
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans