import math,random
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

def countSort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    countArr = []
    for i in range(length):
        countTemp = 0
        for j in range(length):
            if arr[j] < arr[i]:
                countTemp += 1
        countArr.append(countTemp)
    result = [0]*length
    for i in range(length):
        result[countArr[i]]=arr[i]
    return result

def quickSort(nums):
    if len(arr) == 1:
        return arr
    #初始化两个栈
    startStack = [0,]
    endStack = [len(nums)-1,]

    #进入循环，两个栈均为空时，排序结束
    while startStack and endStack:
        #得到本次循环的start 和 end
        start = startStack.pop()
        end = endStack.pop()
        #判断子数组是否有序
        if start>end:
            continue
        i = start
        j = end
        while i < j:
            if nums[i] > nums[j]:
                nums[i], nums[j-1], nums[j] = nums[j-1], nums[j], nums[i]
                j -= 1
            else:
                i += 1
        #将两个子数组的开始和结尾push进栈中
        startStack.append(start)
        endStack.append(i-1)
        startStack.append(i+1)
        endStack.append(end)
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



if __name__ == '__main__':
    # arr = [9, 8, 7, 6, 78, 4, 3, 2, 89]
    # arr = [0]
    # print(pow(2,3))
    # arr=[8,10,7]
    # arr = [int(x) for x in input().split(' ')]
    # print(' '.join([str(x) for x in insertSort(arr)]))
    # print(' '.join([str(x) for x in bubbleSort(arr)]))
    # print(countSort(arr))
    # quickSort(arr)
    # print(arr)
    # arr = [12,1,8]
    # arr = [12,3,5,0,14]
    arr = random.sample(range(4, 30), 14)
    print(arr)
    mergeSort(arr)
    print(arr)