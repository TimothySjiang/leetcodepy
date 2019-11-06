#Quora OA
def arithmeticLength(a,b):
    lenA = len(a)
    lenB = len(b)
    l, r = 0, lenB
    while l < r:
        mid = l + (r - l) // 2
        if b[mid] < a[0]:
            l = mid + 1
        else:
            r = mid
    pos = l
    res = -1
    print(pos,a,b)
    if len(a) == 1:
        for i in range(lenB):
            res = max(res,findLong(b,a[0],pos,i))
    else:
        diffMax = a[1] - a[0]
        for i in range(1,len(a)):
            diffMax = min(diffMax,a[i] - a[i-1])
        for diff in range(diffMax+1):
            temp = [a[0]]
            if pos == 0:
                idxA, idxB = 1, 0
                while idxA < lenA and idxB < lenB:
                    if a[idxA] == temp[-1] + diff:
                        temp.append(a[idxA])
                        idxA += 1
                    elif b[idxB] == temp[-1]+ diff:
                        temp.append(b[idxB])
                        idxB += 1
                    else:
                        idxB += 1
                if idxA == lenA:
                    addAfter(b,idxB,diff,temp)

            elif pos == lenB:
                i = 1
                while i < len(a) and a[i] - a[i-1] == diff:
                    temp.append(a[i])
                    i += 1
                if i == len(a):
                    addFront(b,len(b)-1,diff,temp)
            else:
                idxA, idxB = 1, pos
                while idxA < lenA and idxB < lenB:
                    if a[idxA] == temp[-1] + diff:
                        temp.append(a[idxA])
                        idxA += 1
                    elif b[idxB] == temp[-1] + diff:
                        temp.append(b[idxB])
                        idxB += 1
                    else:
                        idxB += 1

                while idxA < lenA:
                    if a[idxA] == temp[-1] + diff:
                        temp.append(a[idxA])
                        idxA += 1
                    else:
                        break

                if idxA == lenA:
                    addFront(b,pos-1,diff,temp)
                    addAfter(b,idxB,diff,temp)
            if len(temp) > 1:
                res = max(res,len(temp))
    return res

def findLong(b,val,pos,loc):
    temp = [val]
    diff = abs(val - b[loc])
    res = 0
    if pos == 0:
        addAfter(b,0,diff,temp)
    elif pos == len(b):
        addFront(b,pos - 1,diff,temp)
    else:
        addFront(b, pos - 1, diff, temp)
        addAfter(b,pos,diff,temp)
    res = max(res,len(temp))
    return res

def addAfter(b,idxB,diff,temp):
    while idxB < len(b):
        if b[idxB] == temp[-1] + diff:
            temp.append(b[idxB])
        idxB += 1

def addFront(b,idxB,diff,temp):
    while idxB >= 0:
        if b[idxB] == temp[0] - diff:
            temp.insert(0,b[idxB])
        idxB -= 1


if __name__ == '__main__':
    print(arithmeticLength( [28,30],[5,7,12,16,20,24]))