class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+': lambda a, b: a + b,
                    "-": lambda a, b: a - b,
                    "*": lambda a, b: a * b,
                    "/": lambda a, b: int(a / b)}
        for c in tokens:
            if c not in operator:
                stack.append(int(c))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operator[c](a, b))

        return stack[0]