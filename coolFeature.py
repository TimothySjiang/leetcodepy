#Quora OA
import collections
def coolFeature(a,b,queries):
    counter = collections.Counter(a)
    res = []
    for query in queries:
        if len(query) == 2:
            res.append(findSum(counter,b,query[1]))
        else:
            b[query[1]] = query[2]
    return res

def findSum(map,b,target):
    res = 0
    for num in b:
        res += map[target-num]
    return res

if __name__ == '__main__':
    print(coolFeature([1,2,3],[3,4],[[1, 5], [1, 1 , 1], [1, 5]]))