class Solution(object):
    def kSimilarity(self, A, B):
        queue = [A]
        seen = {A: 0}
        while queue:
            S = queue.pop(0)
            if S == B: return seen[S]
            for T in self.neighbors(S, B):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

    def neighbors(self, S, B):
        for i, c in enumerate(S):
            if c != B[i]:
                break

        T = list(S)
        for j in range(i + 1, len(S)):
            if S[j] == B[i]:
                T[i], T[j] = T[j], T[i]
                yield "".join(T)
                T[j], T[i] = T[i], T[j]