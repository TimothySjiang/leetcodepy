class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        A = list(A)
        B = list(B)
        queue = [(B,0)]
        level = 0
        visited = set()
        visited.add(tuple(B))
        while queue:
            for i in range(len(queue)):
                node,p = queue.pop(0)
                if node == A:
                    return level
                while p < len(A) :
                    if A[p] != node[p]:
                        for j in range(p + 1,len(node)):
                            if node[j] == A[p]:
                                newnode = node[:]
                                newnode[p],newnode[j] = newnode[j],newnode[p]
                                if tuple(newnode) not in visited:
                                    visited.add(tuple(newnode))
                                    queue.append((newnode,p+1))
                        break
                    else:
                        p += 1
            level += 1

