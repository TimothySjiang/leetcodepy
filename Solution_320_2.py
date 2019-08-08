class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def Nums(s):
            count = 0
            for i in range(len(s)):
                if s[i].isalpha():
                    break
                count += 1
            return count

        def helpGenerate(word):
            if not word: return [""]
            rest = helpGenerate(word[1:])
            res = [word[0] + x for x in rest]
            for s in rest:
                count = Nums(s)
                if not count:
                    res.append("1" + s)
                else:
                    res.append(str(1 + int(s[:count])) + s[count:])
            return res

        return helpGenerate(word)

