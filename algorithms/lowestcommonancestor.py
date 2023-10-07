# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        def helper(node, minn, maxn):
            if minn <= node.val <= maxn:
                return node

            if node.val > maxn:
                return helper(node.left, minn, maxn)

            if node.val < minn:
                return helper(node.right, minn, maxn)

        return helper(root, p.val, q.val)