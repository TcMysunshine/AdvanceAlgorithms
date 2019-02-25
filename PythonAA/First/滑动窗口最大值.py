from collections import deque


def slidingWindowMax(arr,w):
    length = len(arr)
    qmax = deque()
    res = []
    for i in range(length):
        while qmax and arr[qmax[-1]]<=arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] == i - w:
            qmax.popleft()
        if i >= w-1:
            res.append(arr[qmax[0]])
    return res


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 3, 3, 6, 7]
    w = 3
    print(slidingWindowMax(arr, w))

