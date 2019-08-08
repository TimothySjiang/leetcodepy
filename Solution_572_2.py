class Solution(object):
    def isSubtree(self, s, t):
        if self.isMatch(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.isMatch(root1.left, root2.left) and self.isMatch(root1.right, root2.right)