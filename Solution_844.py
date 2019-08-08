class Solution_844:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)

        j1 = 0
        for i in range(len(S)):
            if S[i] != '#':
                S[j1] = S[i]
                j1 += 1

            else:
                j1 =max(j1-1,0)


        j2 = 0
        for i in range(len(T)):
            if T[i] != "#":
                T[j2] = T[i]
                j2 += 1
            else:
                j2 =max(j2-1,0)



        return S[0:j1]==T[0:j2]