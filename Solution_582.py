class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = collections.defaultdict(list)
        for i in range(len(pid)):
            d[ppid[i]].append(pid[i])
        res = []
        queue = [kill]
        while queue:
            p = queue.pop()
            res.append(p)
            queue += d[p]

        return res