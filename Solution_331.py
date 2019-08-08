class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [0]
        preorder = preorder.split(',')
        low = float('-inf')

        for i, val in enumerate(preorder):
            if val != "#":
                stack.append(int(val))
            else:
                stack.pop()
                if not stack and i != len(preorder) - 1:
                    return False

        return stack == []