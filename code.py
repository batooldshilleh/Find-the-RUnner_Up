if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_arngment = sorted(list(arr))
    print(arr_arngment[-3])
