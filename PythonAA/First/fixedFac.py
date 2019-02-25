def hashSolve(arr,sumValue):
    hashMapArr = {}
    for i in range(len(arr)):
        hashMapArr[arr[i]] = i
    # print(hashMapArr)
    resultHash = {}
    # print(hashMapArr.get(3))
    for i in range(len(arr)):
        temp = sumValue - arr[i]
        if hashMapArr.__contains__(temp):
            if arr[i] < temp:
                if resultHash.get(arr[i]) is None:
                    resultHash[arr[i]] = temp
    print(len(resultHash))

def solve2(arr,sumValue):

    hashMapArr = {}
    for i in range(len(arr)):
        hashMapArr[arr[i]] = i
    # print(hashMapArr)
    resultList = []
    count = 0
    # print(hashMapArr.get(3))
    for i in range(len(arr)):
        temp = sumValue - arr[i]
        if hashMapArr.__contains__(temp):
            if arr[i] in resultList or temp in resultList:
                pass
            else:
                print(arr[i])
                resultList.append(arr[i])
                count += 1
    # print(resultList)
    print(count)


if __name__ == '__main__':
    arr = [1, 2, 4, 7, 11, 0, 9, 15]
    sumValue = 11
    # arr = [int(x) for x in input().split(" ")]
    # sumValue = int(input())
    # hashSolve(arr, sumValue)
    solve2(arr,sumValue)


