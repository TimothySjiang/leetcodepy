class Solution_58:
    def lengthOfLastWord(self, s: str) -> int:
        sR = s.strip()[::-1]
        index = sR.find(" ")
        if (index == -1):
            return len(sR)
        return index