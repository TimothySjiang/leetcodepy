#Quora OA
def arithmeticLength(a,b):
    lenA, lenB, res = len(a),len(b),-1
    if len(a) == 1:
        for i in range(lenB):
            front = countFront(b, a[0], abs(b[i]-a[0]))
            after = countAfter(b, a[0], abs(b[i]-a[0]))
            res = max(res,front+after+1)
    else:
        diffMax = a[1] - a[0]
        for i in range(1,len(a)):
            diffMax = min(diffMax,a[i] - a[i-1])
        for diff in range(diffMax+1):
            temp = [a[0]]
            idxA,idxB = 1, 0
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
                front = countFront(b,temp[0],diff)
                after = countAfter(b,temp[-1],diff)
                res = max(res,front+len(temp)+after)
    return res

def countAfter(b,startVal,diff):
    count = 0
    for i in range(len(b)):
        if b[i] == startVal + diff:
            count += 1
            startVal += diff
    return count

def countFront(b,startVal,diff):
    count = 0
    for i in range(len(b)-1,-1,-1):
        if b[i] == startVal - diff:
            count += 1
            startVal -= diff
    return count

if __name__ == '__main__':
    print(arithmeticLength([0,4,8,20],[5,7,12,16,20,24]))