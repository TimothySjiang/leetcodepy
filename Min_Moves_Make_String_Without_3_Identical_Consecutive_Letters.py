def count(str):
    count = 0
    i = 0
    while i < len(str)-2:
        if str[i] == str[i+1] and str[i] == str[i+2]:
            j = i+3
            while j < len(str) and str[j] == str[i]:
                j += 1
            count += (j-i)//3
            i = j
        else:
            i += 1
    return count


def main():
    print(count('baaaaa'))
    print(count('baaabbaabbba'))
    print(count('baabab'))


if __name__ == "__main__":
    main()