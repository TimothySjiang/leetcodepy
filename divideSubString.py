#Quora OA
def divideSuvString(n,k):
    n, count = str(n), 0
    seen = set()
    for i in range(len(n)-k+1):
        if n[i:i+k] not in seen and not int(n) % int(n[i:i+k]):
            seen.add(n[i:i+k])
            count += 1
    return count


if __name__ == '__main__':
    print(divideSuvString(555,1))