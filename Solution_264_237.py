def numbers(k):
    res = []
    p1 = p2 = p3 = 0
    n1 = n2 = n3 = 1
    for i in range(k+1):
        num = min(n1,n2,n3)
        res.append(num)
        if num == n1:
            n1 = res[p1] * 2
            p1+=1
        if num == n2:
            n2 = res[p2] * 3
            p2 += 1
        if num == n3:
            n3 = res[p3] * 7
            p3 += 1
    return res[-1]