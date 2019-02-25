def getMiddle(list,low,high):
    tmp = list[low]
    while low < high:
        while low < high and list[high] > tmp:
            high -= 1
        list[low] = list[high]

        while low < high and list[low] < tmp:
            low += 1
        list[high] = list[low]
    list[low] = tmp
    return low

def quickSort1(list,low,high):
    if low >= high:
        return
    middle = getMiddle(list, low, high)
    quickSort1(list, low, middle-1)
    quickSort1(list, middle+1, high)

def qsort(arr):
    if not len(arr):
        return []
    else:
    # 在这里以第一个元素为基准线
        pivot = arr[0]
        left = qsort([x for x in arr[1:] if x < pivot])
        right = qsort([x for x in arr[1:] if x >= pivot])
    return left+[pivot]+right
if __name__ == '__main__':
    list = [7,4,3,1,9,8,6,5]
    # getMiddle(list, 0, len(list)-1)
    # print(list)
    quickSort1(list, 0, len(list)-1)
    print(list)