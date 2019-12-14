class Solution:
    def expand(self, S: str) -> List[str]:
        results = []
        self.backtrack(S, 0, "", results)
        return sorted(results)

    def backtrack(self, s, start, word, results):
        if start == len(s):
            results.append(word)
        else:
            if s[start] == "{":
                j = start + 1
                while s[j] != '}':
                    j += 1
                for letter in s[start + 1:j].split(','):
                    self.backtrack(s, j + 1, word + letter, results)
            else:
                self.backtrack(s, start + 1, word + s[start], results)