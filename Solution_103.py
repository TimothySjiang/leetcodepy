# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        temp = []
        p = [root]
        flag= 1
        while p:
            for i in range(len(p)):
                node=p.pop(0)
                temp+=[node.val]
                if node.left: p+=[node.left]
                if node.right: p+=[node.right]
            result+=[temp[::flag]]
            temp=[]
            flag*=-1
        return result