class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if (len(num1) == 0 and len(num2) == 0): return ""
        if len(num1) == 0: return num2
        if len(num2) == 0: return num1

        if ord(num1[-1]) - ord("0") + ord(num2[-1]) - ord("0") >= 10:
            return self.addStrings(self.addStrings(num1[0:-1], num2[0:-1]), "1") + str(
                (ord(num1[-1]) + ord(num2[-1]) - 2 * ord("0")) % 10)
        else:
            return self.addStrings(self.addStrings(num1[0:-1], num2[0:-1]), "") + str(int(num1[-1]) + int(num2[-1]))
