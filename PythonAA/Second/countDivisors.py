import math


def countDivisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1):
        if (n % i == 0):
            # If divisors are equal,
            # count only one
            if n / i == i:
                cnt = cnt + 1
            else:  # Otherwise count both
                cnt = cnt + 2
    return cnt


if __name__ == '__main__':
    testCase = int(input())
    list = []
    for i in range(testCase):
        list.append(int(input()))
    for x in list:
        cnt = 0
        for t in range(x):
            countD9 = countDivisors(t)
            if countD9 == 9:
                cnt += 1
        print(cnt)