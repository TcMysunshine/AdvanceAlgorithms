def histogram1(arr):
    length = len(arr)
    maxArea = 0
    for i in range(length):
        left = i
        right = i
        while left >= 0 and arr[left] >= arr[i]:
            left -= 1
        while right < length and arr[right] >= arr[i]:
            right += 1
        maxArea = max(arr[i] * (right - left - 1), maxArea)
    return maxArea


def stackhistogram(arr):
    length = len(arr)
    maxArea = 0
    stack = []
    i = 0
    while i < length:
        # print("i->"+str(i)+"->"+str(arr[i]))
        if len(stack) == 0 or arr[i] > arr[stack[len(stack) - 1]]:
            # if len(stack)>0:
            #     print(stack[len(stack)-1])
            stack.append(i)
        else:
            popNum = stack.pop()
            if len(stack) == 0:
                tempArea = i * arr[popNum]
                # print(str(popNum) + ":"+str(arr[popNum]))
            else:
                tempArea = (i - stack[len(stack) - 1] - 1) * arr[popNum]
                # print(str(i) + ":"+str(stack[len(stack)-1]) + ":" + str(arr[popNum]))
            # print("Area->"+str(tempArea))
            if tempArea > maxArea:
                maxArea = tempArea
            i -= 1
        i += 1
    while len(stack) != 0:
        popNum = stack.pop()
        if len(stack) == 0:
            tempArea = length * arr[popNum]
        else:
            tempArea = (length - stack[len(stack) - 1] - 1) * arr[popNum]
        if tempArea > maxArea:
            maxArea = tempArea
    return maxArea


def ma2his(arr):
    row = len(arr)
    col = len(arr[0])
    height = [[0 for x in range(col)]] * row
    height[0] = arr[0]
    maxArea = stackhistogram(height[0])
    for i in range(1, row):
        for j in range(col):
            if arr[i][j] == 0:
                height[i][j] = 0
            else:
                height[i][j] = height[i - 1][j] + 1
        maxArea = max(maxArea, stackhistogram(height[i]))
    return maxArea


if __name__ == '__main__':
    # # arr = [2, 7, 9, 4, 1]
    # arr = [2, 3, 5, 6, 2, 3]
    # # print(arr.pop())
    # print(arr)
    # # print(histogram1(arr))
    # print(stackhistogram(arr))
    import sys
    arr=[]
    while True:
        line = input()
        if line == '' or line is None:
            break
        arr.append([int(x) for x in line.split(" ")])
    print(ma2his(arr))
    # arr = [
    #     [1, 0, 1, 1],
    #     [1, 1, 1, 1],
    #     [1, 1, 1, 0]
    # ]
    # print(ma2his(arr))