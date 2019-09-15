class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        stack = []
        flag = False
        for i in range(len(n)-1,-1,-1):
            j = i
            while stack and stack[-1] > n[i]:
                stack.pop()
                j += 1
                flag = True
            if flag: break
            stack.append(n[i])
        if j:
            tmp = n[i]
            n[i] = n[j]
            n[j] = tmp
            ans =  "".join(n[:i+1] + n[i+1:][::-1])
            if int(ans) > 2**31-1:
                return -1
            else:
                return ans
        return -1