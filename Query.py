#Quora OA
import collections
def query(arr,queries):
    res = 0
    indexs = collections.defaultdict(list)
    for i in range(len(arr)):
        indexs[arr[i]].append(i)
    for query in queries:
        index = indexs[query[2]]
        l = 0
        r = len(index) + 1
        while l < r:
            mid = l + (r-l)//2
            if index[mid] < query[0]:
                l = mid + 1
            else:
                r = mid
        left = l
        r = len(index)
        while l < r:
            mid = l + (r-l)//2
            if index[mid] <= query[1]:
                l = mid + 1
            else:
                r = mid
        res += (l - left)

    return res

if __name__ == '__main__':
    print(query([1,1,2,3,2], [[1,2,1], [2,4,2], [0,3,1]]))