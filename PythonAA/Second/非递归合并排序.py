import math
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    count = math.ceil(math.log(length,2))
    for i in range(count):
        x = pow(2, i)
        # j = 0
        low = 0
        while low < length:
            mid = low + x
            high = min(mid + x, length)
            merge(arr, low, mid, high)
            low = low + 2 * x
def merge(arr,start,mid,end):
    i, j = start, mid
    result = []
    while i < mid and j < end:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1
    result += arr[i:mid]
    result += arr[j:end]
    arr[start:end] = result[0:end-start]


if __name__ =='__main__':
    while True:
        try:
            arr = [int(x) for x in input().split(' ')]
            mergeSort(arr)
            print(' '.join([str(x) for x in arr]))
        except EOFError:
            break