class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip().lower()

        if not s:
            return False

        for i, char in enumerate(s):
            if ord('a') <= ord(char) <= ord('z') and char != 'e':
                return False

            if char in ['+', "-"] and i:
                return False

            if char == 'e' and (i == len(s) - 1 or not i):
                return False

        return True


