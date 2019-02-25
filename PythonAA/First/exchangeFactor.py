def exchangeFactor(arr1,arr2):
    sumArr1 = sum(arr1)
    sumArr2 = sum(arr2)
    diff = sumArr1 - sumArr2
    lenArr1 = len(arr1)
    lenArr2 = len(arr2)
    while diff != 0:
        bestChange,besti,bestj = 0, 0, 0
        for i in range(lenArr1):
            for j in range(lenArr2):
                exchangeDiff = arr1[i]-arr2[j]
                if abs(diff-2 * exchangeDiff) < abs(diff-2 * bestChange):
                    besti, bestj, bestChange = i, j, exchangeDiff
        if bestChange == 0:
            return False
        temp = arr1[besti]
        arr1[besti] = arr2[bestj]
        arr2[bestj] = temp
        sumArr1 = sumArr1 - bestChange
        sumArr2 = sumArr2 + bestChange
        diff = sumArr1-sumArr2
    return True


if __name__ == '__main__':
    # arr1 = [100, 20, 98, 1, 2, 3]
    # arr2 = [1, 2, 3, 4, 5, 45]
    arr1 = [int(x) for x in input().split(" ")]
    arr2 = [int(x) for x in input().split(" ")]
    exchangeFactor(arr1, arr2)
    print(sum(arr1)-sum(arr2))
