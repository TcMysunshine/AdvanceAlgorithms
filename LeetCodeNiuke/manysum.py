arr = [1, 2, 4, 1, 7, 8, 3]
S = 9


def findNotNearMax(arr):
    length = len(arr)
    opt = [0] * length
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, length):
        opt[i] = max(opt[i - 2] + arr[i], opt[i - 1])
    return opt


def findPath(opt, arr, i):
    x = [0] * len(arr)
    j = i
    aim = opt[i]
    while arr[j] != aim:
        aim -= arr[j]
        if opt[j] == opt[j - 1]:
            x[j] = 0
            j = j - 1
        elif opt[i] == opt[i - 2] + arr[i]:
            x[j] = 1
            j = j - 2
    # x[j] = 1
    return x
    # if i==1
    # if opt[i] == opt[i - 1]:
    #     x[i] = 0
    #     findPath(opt, arr, i - 1)
    # elif opt[i] == opt[i - 2] + arr[i]:
    #     x[i] = 1
    #     findPath(opt, arr, i - 2)


print(arr)
opt = findNotNearMax(arr)
print(opt)
k = 5
path = findPath(opt, arr, k)
print(path)
showIndex = []
for i in range(len(path)):
    if path[i] == 1:
        showIndex.append(i)
print(" ".join([str(arr[x]) for x in showIndex]))
