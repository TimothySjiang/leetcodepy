class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def helpGenerate(word):
            if not word: return [""]
            rest = helpGenerate(word[1:])
            res = [word[0] + x for x in rest]
            for s in rest:
                if not s or s[0].isalpha():
                    res.append("1" + s)
                else:
                    count = 0
                    for i in range(len(s)):
                        if s[i].isalpha():
                            break
                        count += 1
                    res.append(str(1 + int(s[:count])) + s[count:])

            return res

        return helpGenerate(word)
