def stackhistogram(arr):
    length = len(arr)
    maxArea = 0
    stack = []
    i = 0
    while i < length:
        if len(stack) == 0 or arr[i] > arr[stack[len(stack) - 1]]:
            stack.append(i)
        else:
            popNum = stack.pop()
            if len(stack) == 0:
                tempArea = i * arr[popNum]
            else:
                tempArea = (i - stack[len(stack) - 1] - 1) * arr[popNum]
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


def subMax(arr):
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
    arr = []
    try:
        while True:
            line = input()
            arr.append([int(x) for x in line.split(" ")])
    except EOFError:
        # print(arr)
        print(subMax(arr))
# while True:
#     line = input()
#     if line == '' or line is None:
#         break
#     arr.append([int(x) for x in line.split(" ")])
# print(subMax(arr))

# arr = []
# while True:
#     line = input()
#     if line == '' or line is None:
#         print(ma2his(arr))
#         arr = []
#     else:
#         arr.append([int(x) for x in line.split(" ")])
