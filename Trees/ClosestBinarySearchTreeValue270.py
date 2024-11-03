# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        def helper(node, target, closest):
            if not node:
                return closest
            
            # check if closer than closest and update
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
                
                
            if abs(node.val - target) == abs(closest - target):
                closest = min(node.val, closest)
            
            if target > node.val:
                return helper(node.right, target, closest)
            else:
                return helper(node.left, target, closest)
        
        return helper(root, target, root.val)
        