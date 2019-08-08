class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [""]
        for i in range(1, n + 1):
            if i == 1:
                result = set("")
                result.add("()")
                continue

            result2 = set()
            for p in result:
                for j in range(i + 1):
                    result2.add(p[0:j] + "()" + p[j:])
                result = result2

        return list(result)