def insertSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    for i in range(1, length):
        j = i
        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr


if __name__ == '__main__':
    arr = [int(x) for x in input().split(' ')]
    print(' '.join([str(x) for x in insertSort(arr)]))