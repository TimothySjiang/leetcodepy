# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        queue = [root]
        result = []
        while queue:
            p = queue.pop(0)
            if p:
                result.append(p.val)
                queue.append(p.left)
                queue.append(p.right)
            else:
                result.append('null')

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 2:
            return None
        data = data[1:-1].split(', ')

        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while i < len(data):
            current = queue.pop(0)
            if data[i] != "'null'":
                current.left = TreeNode(int(data[i]))
                queue.append(current.left)
            i += 1

            if data[i] != "'null'":
                current.right = TreeNode(int(data[i]))
                queue.append(current.right)
            i += 1

        return root


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))