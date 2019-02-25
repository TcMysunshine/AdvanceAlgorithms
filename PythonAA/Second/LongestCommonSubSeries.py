from collections import deque
import copy
import random
def getLIS(arr):
    l2 = len(arr)
    LIS = []
    # first = arr[0]
    LIS.append([0])
    for i in range(1, l2):
        temp = [i]
        maxLength = 0
        for x in LIS:
            if arr[i] > arr[x[-1]]:
                maxLength = max(maxLength, len(x))
        if maxLength == 0:
            LIS.append(temp)
        else:
            # 加入到最长的哪一个里面
            tempLIS = []
            for x in LIS:
                if len(x) == maxLength and arr[i] > arr[x[-1]]:
                    temp = x + temp
                    tempLIS.append(temp)
                    temp = [i]
            for y in tempLIS:
                LIS.append(y)
    return LIS


def getLIDSIndex(arr):
    length = len(arr)
    lisMax = [1] * length
    ldsMax = [1] * length
    for i in range(1, length):
        for j in range(i):
            if arr[i] > arr[j] and lisMax[i] < lisMax[j] + 1:
                lisMax[i] = lisMax[j] + 1
        m = length - i - 1
        for k in range(length - 1, m, -1):
            if arr[m] > arr[k] and ldsMax[m] < ldsMax[k] + 1:
                ldsMax[m] = ldsMax[k] + 1
    result = [0]*length
    for i in range(length):
        result[i] = lisMax[i] + ldsMax[i]
    maxIndex = []
    maxCount = max(result)
    for index in range(length):
        if result[index] == maxCount:
            maxIndex.append(index)
    return maxIndex


def getLDS(arr):
    arr.reverse()
    LDS = getLIS(arr)
    for x in LDS:
        for i in range(len(x)):
            x[i] = len(arr) - x[i] -1
    return LDS

def getLISLDS(arr):
    LIDSIndex = getLIDSIndex(arr)
    LIS = getLIS(arr)
    LDS = getLDS(arr)
    for lds in LDS:
        lds.reverse()
    result = []
    arr.reverse()
    for lidsindex in LIDSIndex:
        # tempEnding = arr[lidsindex]
        for lis in LIS:
            if lis[-1] == lidsindex:
                for lds in LDS:
                    if lds[0] == lidsindex:
                        result.append(lis + lds[1:])
    for tempResult in result:
        print(" ".join([str(arr[x]) for x in tempResult]))


def idS(arr):
    queue = deque()
    result = deque()
    queue.append({"i": 0, "list": [arr[0]]})
    queue.append({"i": 0, "list": []})
    while queue:
        t = queue.popleft()
        i = t['i']
        l = copy.copy(t['list'])
        i += 1
        if i <= len(arr):
            if i == len(arr):
                j = 1
                while j < len(l):
                    if l[j] <= l[j-1]:
                        break
                    j += 1
                flag = True
                while j < len(l):
                    if l[j] >= l[j - 1]:
                        flag = False
                        break
                    j += 1
                if flag:
                    while result and len(result[-1]) < len(l):
                        result.pop()

                    if result:
                        if len(result[-1]) == len(l):
                            result.append(l)
                    else:
                        result.append(l)
            else:
                if result:
                    if len(result[0]) > len(l) + len(arr) - i:
                        continue
                queue.append({"i": i, "list": l})
                c = copy.copy(l)
                c.append(arr[i])
                queue.append({"i": i, "list": c})
    while result:
        print(" ".join(str(item) for item in result[-1]))
        result.pop()
    # return result


if __name__ == '__main__':
    arr = random.sample(range(4, 30), 14)
    # arr = [17, 18, 7, 10, 14, 14, 1, 11, 3]
    # arr = [1,2,3,4]
    print(arr)
    print("-------CH-------")
    getLISLDS(arr)
    print("-------LXJ----------")
    idS(arr)
    # getLDS(arr)
    # getAllLIS(arr)


