#https://leetcode.com/discuss/interview-question/387951/microsoft-oa-2019 Q3
class Solution():
    def totalChars(self, string):
        if "aaa" in string: return -1
        for i in range(len(string) + 1):
            if self.safe(string, i):
                newString = string[:i] + 'a' + string[i:]
                res = self.recursion(newString, i + 1)
                return len(res) - len(string)
        return 0

    def recursion(self, string, start):
        if start == len(string) - 1 and string[-2:] == "aa":
            return string
        for i in range(start, len(string) + 1):
            if self.safe(string, i):
                newString = string[:i] + 'a' + string[i:]
                res = self.recursion(newString, i + 1)
                return res
        return string

    def safe(self, string, i):
        if i < len(string) - 1 and string[i:i + 2] == 'aa':
            return False
        if 0 < i < len(string) and string[i - 1:i + 1] == 'aa':
            return False
        if i > 1 and string[i - 2:i] == 'aa':
            return False
        return True


obj = Solution()
print(obj.totalChars('aabab'))
print(obj.totalChars('dog'))
print(obj.totalChars('aa'))
print(obj.totalChars('baaaa'))
print(obj.totalChars('a'))
print(obj.totalChars('ab'))
print(obj.totalChars(''))