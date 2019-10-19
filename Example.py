def validParenthesis(parenthesis):
    dict = {'[':']','{':'}','(':')'}
    stack = []
    for p in parenthesis:
        if p in dict:
            stack.append(p)
        else:
            if not stack: return False
            preP = stack.pop()
            if dict[preP] != p:
                return False

    return True if not stack else False


if __name__ == "__main__":
    print(validParenthesis([]))
    print(validParenthesis(['(']))
    print(validParenthesis([')']))
    print(validParenthesis((['(',')'])))
