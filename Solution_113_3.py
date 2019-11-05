# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        results = []
        self.helpSum(sum, root, [], results)
        return results

    def helpSum(self, target, node, result, results):
        if target - node.val == 0 and not node.left and not node.right:
            results.append(result + [node.val])
        else:
            if node.left:
                result.append(node.val)
                self.helpSum(target - node.val, node.left, result, results)
                result.pop()
            if node.right:
                result.append(node.val)
                self.helpSum(target - node.val, node.right, result, results)
                result.pop()