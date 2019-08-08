class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        operator = set({'+', 'D', 'C'})
        for r in ops:
            if r not in operator:
                stack.append(int(r))

            if r == 'C':
                stack.pop()
            if r == "D":
                stack.append(2 * stack[-1])
            if r == "+":
                stack.append(stack[-2] + stack[-1])

        return sum(stack)