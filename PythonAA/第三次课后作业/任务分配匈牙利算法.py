import numpy as np
from scipy.optimize import linear_sum_assignment
'''输入的转化为cost矩阵'''
def arr2matrix(arr, workCount):
    person = []
    for x in arr:
        if x[0] not in person:
            person.append(x[0])
    row = len(person)
    col = workCount
    matrix = [[0 for j in range(col)] for i in range(row)]
    for x in arr:
        matrix[x[0]-1][x[1]-1] = x[2]
    mat = np.array(matrix)
    print(mat)
    return mat

'''每一行减去最小值'''
def rowGY(mat, row):
    for i in range(row):
        mat[i] = mat[i]-min(mat[i])
    print(mat)
    return mat

'''每一列减去最小值'''
def colGY(mat, col):
    for j in range(col):
        mat[:, j] = mat[:, j]-min(mat[:, j])
    print(mat)
    return mat

def apiXyl(matrix):
    arr = [[2, 1, 6], [1, 2, 2],
           [1, 3, 7], [1, 4, 8],
           [1, 1, 9], [2, 2, 4],
           [2, 3, 3], [2, 4, 7],
           [3, 1, 5], [3, 2, 8],
           [3, 3, 1], [3, 4, 8],
           [4, 1, 7], [4, 2, 6],
           [4, 3, 9], [4, 4, 4]]
    cost = np.array(arr2matrix(arr, 4))
    row_ind, col_ind = linear_sum_assignment(cost)
    print(row_ind)  # 开销矩阵对应的行索引
    print(col_ind)  # 对应行索引的最优指派的列索引
    print(cost[row_ind, col_ind])  # 提取每个行索引的最优指派列索引所在的元素，形成数组
    print(cost[row_ind, col_ind].sum())  # 数组求和


if __name__ == '__main__':
    arr = [[2, 1, 6], [1, 2, 2],
           [1, 3, 7], [1, 4, 8],
           [1, 1, 9], [2, 2, 4],
           [2, 3, 3], [2, 4, 7],
           [3, 1, 5], [3, 2, 8],
           [3, 3, 1], [3, 4, 8],
           [4, 1, 7], [4, 2, 6],
           [4, 3, 9], [4, 4, 4]]
    mat = arr2matrix(arr, 4)
    apiXyl(mat)
