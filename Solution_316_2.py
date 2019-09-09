class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        loc = {c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c not in visited:
                while stack and stack[-1] > c and i < loc[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                visited.add(c)
        return ''.join(stack)
