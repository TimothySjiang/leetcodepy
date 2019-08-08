class Solution_383:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        t = [0] * 26
        for i in magazine:
            index = ord(i) - ord('a')
            t[index] += 1

        for i in ransomNote:
            index = ord(i) - ord('a')
            t[index] -= 1
            if t[index] < 0:
                return False

        return True