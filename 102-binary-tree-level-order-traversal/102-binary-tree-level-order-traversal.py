# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result: List[List[int]] = []
        lay = [root]
        while lay:
            lay_values = []
            next_lay = []
            
            for node in lay:
                lay_values.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)
            
            lay = next_lay
            result.append(lay_values)
        
        return result
        