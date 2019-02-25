# 求出平面中距离最近的点对（若存在多对，仅需求出一对）
import random
import math


# global resultList

# 计算两点的距离
def calDis(seq):
    dis = math.sqrt((seq[0][0] - seq[1][0]) ** 2 + (seq[0][1] - seq[1][1]) ** 2)
    return dis


# 生成器：生成横跨跨两个点集的候选点
def candidateDot(u, right, dis, med_x):
    cnt = 0
    # 遍历right（已按横坐标升序排序）。若横坐标小于med_x-dis则进入下一次循环；若横坐标大于med_x+dis则跳出循环；若点的纵坐标好是否落在在[u[1]-dis,u[1]+dis]，则返回这个点
    for v in right:
        if v[0] < med_x - dis:
            continue
        if v[0] > med_x + dis:
            break
        if v[1] >= u[1] - dis and v[1] <= u[1] + dis:
            yield v


# 求出横跨两个部分的点的最小距离
def combine(left, right, resMin, med_x,resultList):
    dis = resMin[1]
    minDis = resMin[1]
    pair = resMin[0]
    if len(resultList) == 0:
        resultList.append([pair, minDis])
    for u in left:
        if u[0] < med_x - dis:
            continue
        for v in candidateDot(u, right, dis, med_x):
            dis = calDis([u, v])
            if dis < minDis:
                minDis = dis
                pair = [u, v]
                if minDis < resultList[0][1]:
                    resultList.pop(0)
                    resultList.append([pair, minDis])
                    resultList = sorted(resultList, key=lambda x: x[1], reverse=True)
            elif dis == minDis:
                resultList.append([[u, v], minDis])
                resultList = sorted(resultList, key=lambda x: x[1], reverse=True)
    return [pair, minDis]


# 分治求解
def divide(seq):
    # 求序列元素数量
    n = len(seq)
    # 按点的第一维升序排序
    seq = sorted(seq)
    # 递归开始进行
    if n <= 1:
        return None, float('inf')
    elif n == 2:
        return [seq, calDis(seq)]
    else:
        half = int(len(seq) / 2)
        med_x = (seq[half][0] + seq[-half - 1][0]) / 2
        left = seq[:half]
        resLeft = divide(left)
        right = seq[half:]
        resRight = divide(right)
        # 获取两集合中距离最短的点对
        if resLeft[1] < resRight[1]:
            resMin = combine(left, right, resLeft, med_x,resultList)
        else:
            resMin = combine(left, right, resRight, med_x,resultList)
        pair = resMin[0]
        minDis = resMin[1]
        # resultList.append([pair,minDis])
    return [pair,minDis]


# seq = [(random.randint(0, 10), random.randint(0, 10)) for x in range(10)]
# arr = [
#     [1, 1],
#     [2, 2],
#     [3, 3],
#     [4, 4],
#     [5, 5],
#     [1.5, 1.5]
# ]
# # arr = [
# #     (1, 1),
# #     (2, 2),
# #     (3, 3),
# #     (4, 4),
# #     (5, 5),
# #     (1.5, 1.5)
# # ]1
# # print(seq)
# print("优化算法", divide(arr))
# print(resultList)
def f2s(x):
    return '{:g}'.format(x)


if __name__ == '__main__':
    # x = '{:g}'.format(1.0)
    # print(x)
    num = int(input())
    results = []
    for i in range(num):
        resultList = []
        data = []
        arr = [x for x in input().split(",")]
        for t in arr:
            data.append([float(x) for x in t.split(" ")])
        finalResult =divide(data)
        minDis = finalResult[1]
        result=[]
        for x in resultList:
            if x[1]==minDis:
                result.append(x[0])
        result=sorted(result,key=lambda x:x[0][1])
        # print(result)
        resultStr = ""
        for r in result:
            resultStr+=" ".join([f2s(x) for x in r[0]])+","+" ".join([f2s(x) for x in r[1]])+","
        results.append(resultStr)
    for x in results:
        print(x[0:len(x)-1])

