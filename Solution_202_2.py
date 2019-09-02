class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            newn = 0
            while n:
                newn += (n%10)**2
                n = (n-n%10)//10
            if newn == 1:
                return True
            n = newn
        return False