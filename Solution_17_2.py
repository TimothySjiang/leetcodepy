class Solution:
    def letterCombinations(self, digits):
        if not digits: return []
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        results = []
        self.recursion(digits, dic, 0, '', results)
        return results

    def recursion(self, digits, dic, pos, result, results):
        if pos == len(digits):
            results.append(result)
            return
        for i in dic[digits[pos]]:
            self.recursion(digits, dic, pos + 1, result + i, results)
