#Quora OA
def productSum(number):
    total, prod = 0,1
    number = abs(number)
    while number:
        last = number % 10
        number //= 10
        prod *= last
        total += last

    return prod - total

if __name__ == "__main__":
    print(productSum(44))
    #bug with negative number:
    print(productSum(-44))
