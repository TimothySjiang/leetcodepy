class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0 for i in range(n)]
        lasttime = 0
        for log in logs:
            log = log.split(':')
            Id, status, time = int(log[0]), log[1], int(log[2])
            if status == 'start':
                if stack:
                    res[stack[-1]] += time - lasttime
                stack.append(Id)
            else:
                time += 1
                res[stack.pop()] += time - lasttime
            lasttime = time
        return res
