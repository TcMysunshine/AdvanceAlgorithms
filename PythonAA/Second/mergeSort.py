def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    length = len(arr)
    middle = length // 2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    return merge(left,right)
def merge(left,right):
    result = []
    i, j = 0, 0
    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 78, 4, 3, 2, 89]
    # arr = [int(x) for x in input().split(' ')]
    # print(' '.join([str(x) for x in insertSort(arr)]))
    # print(' '.join([str(x) for x in bubbleSort(arr)]))
    # print(countSort(arr))
    # print(qsort(arr))
    print(mergeSort(arr))
    # print(arr)

