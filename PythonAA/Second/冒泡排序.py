def bubbleSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    for i in range(length-1, 0, -1):
        j = 0
        while j < i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr


if __name__ =='__main__':
    while True:
        try:
            arr = [int(x) for x in input().split(' ')]
            print(' '.join([str(x) for x in bubbleSort(arr)]))
        except EOFError:
            break

