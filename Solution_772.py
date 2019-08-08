class Solution:
    def __init__(self) :
        self.i = 0
    def parseExpr(self ,s) :
        nums = []
        op = '+'
        while self.i < len(s) and op != ')' :   #遇到右括号退出递归
            if s[self.i] == ' ' :
                self.i += 1
                continue
            if s[self.i] == '(' :    	#遇到左括号进入递归
                self.i += 1
                n = self.parseExpr(s)
            else :
                n = self.parseNum(s)	#字符串转化数字
            if  op == '+' :            #加法
                nums.append(n)
            elif op == '-' :			#减法
                nums.append(-n)
            elif op == '*' :			#乘法
                nums[-1] *= n
            elif op == '/' :			#除法
                nums[-1] = int(nums[-1]/n)
            if self.i == len(s) :
                break
            op = s[self.i]
            self.i += 1
        res = 0
        for n in nums :
            res += n
        return res
    def parseNum(self, s) :
        n = 0
        while self.i < len(s) and s[self.i] in '1234567890':
            n = ord(s[self.i]) - ord('0') + 10 * n
            self.i += 1
        return n
    def calculate(self, s):
        return self.parseExpr(s)