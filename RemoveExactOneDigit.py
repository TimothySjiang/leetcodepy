def removeExactOneDigit(s1,s2):
    if not s1 and not s2: return 0
    if not s1: return len(s2)
    if not s2: return 0
    l1, l2, res = len(s1), len(s2), 0
    if s1[0] < s2[0]:
        res = l1 - 1 + l2 - 1
        if s1[1:] < s2 :
            res += 1
        if s1 < s2[1:]:
            res += 1
    elif s1[0] == s2[0]:
        res = removeExactOneDigit(s1[1:],s2[1:])
        if s1[1:] < s2:
            res += 1
        if s1 < s2[1:]:
            res += 1
    else:
        if s1[1:] < s2:
            res = 1
        else:
            res = 0
    return res

if __name__ == '__main__':
    print(removeExactOneDigit('heflo','hhllo'))
    print(removeExactOneDigit('h','hhllo'))
    print(removeExactOneDigit('hf','hhllo'))
    print(removeExactOneDigit('hi','hhllo'))


