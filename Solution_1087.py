class Solution:
    def expand(self, S: str) -> List[str]:
        results = []
        self.backtrack(S, "", results)
        return sorted(results)

    def backtrack(self, s, word, results):
        if not s:
            results.append(word)
        else:
            if s[0] == "{":
                i = s.find("}")
                for letter in s[1:i].split(','):
                    self.backtrack(s[i + 1:], word + letter, results)
            else:
                self.backtrack(s[1:], word + s[0], results)