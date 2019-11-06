#Quora OA
def evenDight(arr):
    count = 0
    for num in arr:
        if not len(str(num)) % 2:
            count += 1
    return count

if __name__ == '__main__':
    print(evenDight([12,3,4,3456]))