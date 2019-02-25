def MaxSubArray(a):
    i, b, sum = 0, 0, 0
    length = len(a)
    while i < length:
        if b > 0:
            b += a[i]
        else:
            b = a[i]
        if b > sum:
            sum = b
        i += 1
    return sum


if __name__ == '__main__':
    a = [1, 2, -3, 4, -2, 5, -3, -1, 7, 4, -6]
    print(MaxSubArray(a))
