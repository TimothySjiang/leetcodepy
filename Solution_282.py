class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        self.recursion(num,target,'',0,0,0,result)
        return result

    def recursion(self,num,target,temp,pos,current,last,result):
        if pos == len(num):
            if current == target:
                result.append(temp)
            return

        for i in range(pos,len(num)):
            if num[pos]=="0" and i!=pos:break
            m = num[pos:i+1]
            value = int(m)
            if not pos:
                self.recursion(num,target,m,i+1,value,value,result)
            else:
                self.recursion(num, target, temp + '+' + m, i + 1, current + value, value, result)
                self.recursion(num, target, temp + '-' + m, i + 1, current - value, -value, result)
                self.recursion(num, target, temp + '*' + m, i + 1, current - last + last * value, last*value, result)