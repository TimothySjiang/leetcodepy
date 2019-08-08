class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {']': '[', '}': '{', ')': '('}
        stack = []
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                try:
                    p = stack.pop()
                except:
                    return False
                if p != dictionary[char]:
                    return False

            else:
                return False

        return stack == []