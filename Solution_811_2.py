class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        c = {}
        for cd in cpdomains:
            n, d = cd.split()
            if d in c.keys():
                c[d] += int(n)
            else:
                c[d] = int(n)
            for i in range(len(d)):
                if d[i] == '.':
                    if d[i + 1:]  in c.keys():
                        c[d[i + 1:]] += int(n)
                    else:
                        c[d[i + 1:]] = int(n)
        return ["%d %s" % (c[k], k) for k in c.keys()]