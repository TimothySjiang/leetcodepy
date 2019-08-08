class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(" ")
        if len(str) != len(pattern):
            return False

        tableP = {}
        tableS = {}

        for i in range(len(pattern)):
            if pattern[i] in tableP:
                if not tableP[pattern[i]] == str[i]:
                    return False
            else:
                tableP[pattern[i]] = str[i]

            if str[i] in tableS:
                if not tableS[str[i]] == pattern[i]:
                    return False
            else:
                tableS[str[i]] = pattern[i]

        return True