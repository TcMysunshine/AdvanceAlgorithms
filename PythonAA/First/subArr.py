from collections import deque
def getSubArrCount(arr, k):
    length = len(arr)
    count = 0
    for i in range(length-1):
        for j in range(i+1, length):
            tempArr = arr[i:j+1]
            # print(tempArr)
            max, min = getMaxMin(tempArr)
            if max-min > k:
                count += 1
    print(count)


def getMaxMin(arr):
    length = len(arr)
    # subArr = []
    max = arr[0]
    min = arr[0]
    for i in range(1,length):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min

# def subArrDeque(arr, k ):
#     count = 0
#     length = len(arr)
#     qmax = deque()
#     qmin = deque()
#     for i in range(length):
#         for j in range(0, length):
#             print(str(i)+"->"+str(j))
#             while qmax and arr[qmax[-1]] < arr[j]:
#                 qmax.pop()
#             while qmin and arr[qmin[-1]] > arr[j]:
#                 qmin.pop()
#             qmax.append(j)
#             qmin.append(j)
#             if arr[qmax[0]] - arr[qmin[0]] <= k:
#                 break
#         if i == qmax[0]:
#             qmax.popleft()
#         if i == qmin[0]:
#             qmin.popleft()
#         count += j - i
#     print(count)


if __name__ == '__main__':
    # arr = [int(x) for x in input().split(" ")]
    # k = int(input())
    arr = [3, 6, 4, 3, 2]
    k = 2
    # subArrDeque(arr,k)
    getSubArrCount(arr, k)

    # print(getMaxMin(arr))

