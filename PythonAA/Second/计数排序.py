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


if __name__ =='__main__':
    arr = [int(x) for x in input().split(' ')]
    print(' '.join([str(x) for x in countSort(arr)]))