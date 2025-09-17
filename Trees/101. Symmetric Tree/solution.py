class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(v1, v2):
            if not v1 and not v2: return True
            if not v1 or not v2: return False
            return v1.val==v2.val and mirror(v1.left, v2.right) and mirror(v1.right, v2.left)
        return mirror(root, root)