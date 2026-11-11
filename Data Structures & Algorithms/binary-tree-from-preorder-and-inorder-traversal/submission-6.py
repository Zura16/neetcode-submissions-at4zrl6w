# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode(None)
        curr = dummy
        i, j, k = 0, 0, len(preorder)
        while i < k and j < k:
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < k and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right = curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < k and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1
        return dummy.right