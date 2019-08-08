class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return self.helpValid(s[i + 1:j + 1]) or self.helpValid(s[i:j])

        return True

    def helpValid(self, s):
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True