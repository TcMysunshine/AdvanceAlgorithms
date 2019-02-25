# -*- coding:utf-8 -*-
'''数组和窗口'''

#
# def getSum(strValue, count):
#     arr = [int(x) for x in strValue.split(" ")]
#     length = len(arr)
#     sum = 0
#     l = length + 1 - count
#     for i in range(l):
#         temparr = arr[i:i + count]
#         # print(temparr)
#         maxValue = max(temparr)
#         sum += maxValue
#     return sum
#
#
# if __name__ == '__main__':
#     import sys
#     for line in sys.stdin:
#         # print(line)
#         count = int(input())
#         print(getSum(line, count))
    # try:
    #     while True:
    #         strValue = raw_input()
    #         count = int(input())
    #         print(getSum(strValue, count))
    # except EOFError:
    #     pass
'''数组和窗口'''
'''汉诺塔'''

def hannuota( n, left, mid, right, start, to):
    if n == 1:
        if start == mid or to == mid:
            return 1
        else:
            return 2
    else:
         num1 = hannuota(n-1, left, mid, right, start, to)
         num2 = hannuota(n-1, left, mid, right, to, start)
         num3 = hannuota(n-1, left, mid, right, start, to)
         return num1+num2+num3+2


if __name__ == '__main__':
    start = 'A'
    mid = 'B'
    end = 'C'
    import sys
    for line in sys.stdin:
        n = int(line)
        print(hannuota(n, start, mid, end, start, end))

'''汉诺塔'''
#     # print("输入：")
# Ente your code here. Read input from STDIN. Print output to STDOUT


# from sys import stdin
# team=[]
# while True:
#     line = stdin.readline().strip()
#     if line=='':
#         break
#     item = line.split(' ')
#     item = [int(i) for i in item]
#     team.append(item)
# print team
