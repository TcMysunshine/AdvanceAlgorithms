def hannuota(n):
    if n == 1:
        return 2
    else:
        return hannuota(n-1)*3 +2


if __name__ == '__main__':
    print(3//2)
    print(3 / 2)
    print((4>>1) -1 )
    # line = input()
    # n = int(line)
    # print(hannuota(n))
    # import sys
    # for line in sys.stdin:
    #     n = int(line)
    #     print(hannuota(n, start, mid, end, start, end))