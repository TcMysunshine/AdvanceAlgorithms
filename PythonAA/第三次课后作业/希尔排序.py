def shell(intervalArr, arr):
    length = len(arr)
    for interval in intervalArr:
        for i in range(interval):
            j = i + interval
            while j < length:
                m = j
                while m >= interval:
                    if arr[m] < arr[m - interval]:
                        arr[m], arr[m - interval] = arr[m - interval], arr[m]
                    m -= interval
                j += interval
    return arr


if __name__ == '__main__':
    # 49 38 65 97 76 13 27 49 55 4
    # 49 38 65 97 26 13 27 49 55 4
    num = int(input())
    results = []
    for i in range(num):
        arr = [int(x) for x in input().split(" ")]
        intervalArr = [int(x) for x in input().split(" ")]
        result = shell(intervalArr, arr)
        results.append(result)
    for res in results:
        print(" ".join([str(x) for x in res]))
