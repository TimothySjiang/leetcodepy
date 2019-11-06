#Quora OA
def sumString(s1,s2):
    if not s1: return s2
    if not s2: return s1
    i1, i2 = len(s1) - 1, len(s2) - 1
    res = ''
    while i1 >= 0 and i2 >= 0:
        ch1 = s1[i1]
        ch2 = s2[i2]
        i1,i2 = i1 - 1, i2 - 1
        res += str(int(ch1) + int(ch2))
    while i1 >= 0:
        res += s1[i1]
        i1 -= 1
    while i2 >= 0:
        res += s2[i2]
        i2 -= 1

    return res[::-1]

if __name__ == '__main__':
    print(sumString('2199','99'))
