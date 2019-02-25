import math


# kd-tree每个结点中主要包含的数据结构如下
class KdNode(object):
    def __init__(self, value=None, split=None, left=None, right=None):
        self.value = value  # k维向量节点(k维空间中的一个样本点)
        self.split = split  # 整数（进行分割维度的序号）
        self.left = left  # 该结点分割超平面左子空间构成的kd-tree
        self.right = right  # 该结点分割超平面右子空间构成的kd-tree


# 构造KD树
def createKDTree(root, data_list):
    length = len(data_list)
    if length == 0:
        return
    d = len(data_list[0])
    split = 0
    max_var = 0
    for i in range(d):
        var = variance(data_list, i)
        if max_var < var:
            max_var = var
            split = i
    data_list.sort(key=lambda x: x[split])
    point = data_list[length // 2]
    root = KdNode(point, split)
    root.left = createKDTree(root.left, data_list[0:length // 2])
    root.right = createKDTree(root.right, data_list[length // 2 + 1:length])
    return root


# 计算点在某个维度上的方差
def variance(data_list, dimension):
    x = []
    sum = 0
    # 某一维度数据长度
    rows = len(data_list)
    for i in range(rows):
        data = data_list[i][dimension]
        x.append(data)
        sum += data
    mean = sum / rows
    vari_sum = 0
    for data in x:
        vari_sum += (data - mean) * (data - mean)
    return vari_sum / rows


def dist(x1, x2):  # 欧式距离的计算
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(x1, x2)))





def f2s(x):
    return '{:g}'.format(x)


def findKNearest(root, target, K):
    global k_nearest_point
    if root == None:
        return
    # 分割的轴
    split = root.split
    # 找到最近的一个点
    if target[split] < root.value[split]:
        findKNearest(root.left, target, K)
    if target[split] > root.value[split]:
        findKNearest(root.right, target, K)
    # 找到最近邻点 轴
    dist1 = dist(root.value, target)
    if len(K_nears) < K:
        K_nears.setdefault(tuple(root.value), dist1)
        k_nearest_point = sorted(K_nears.items(), key=lambda x: x[1], reverse=True)
    elif dist1 <= k_nearest_point[0][1]:
        K_nears.setdefault(tuple(root.value), dist1)
        k_nearest_point = sorted(K_nears.items(), key=lambda x: x[1], reverse=True)
    if root.left != None or root.right != None:
        if abs(target[root.split] - root.value[root.split]) < k_nearest_point[0][1]:
            if target[root.split] < root.value[root.split]:
                findKNearest(root.right, target, K)
            elif target[root.split] > root.value[root.split]:
                findKNearest(root.left, target, K)

    return k_nearest_point


if __name__ == "__main__":
    # data = [
    #     [3, 5],
    #     [6, 2],
    #     [5, 8],
    #     [9, 3],
    #     [8, 6],
    #     [1, 1],
    #     [2, 9]
    # ]
    # root = KdNode()
    # root = createKDTree(root, data)
    # k = 2
    # target = [8.2, 4.6]
    # k_nearest_point = findKNearest(root, target, k)[-k:]
    # print(k_nearest_point)
    num = int(input())
    results = []
    for i in range(num):
        data = []
        K_nears = {}
        # data = [
        #     [3, 5],
        #     [6, 2],
        #     [5, 8],
        #     [9, 3],
        #     [8, 6],
        #     [1, 1],
        #     [2, 9]
        # ]
        k_nearest_point = []
        arr = [x for x in input().split(",")]
        for t in arr:
            data.append([float(x) for x in t.split(" ")])

        target = [float(x) for x in input().split(" ")]
        # target = [8.2, 4.6]
        k = int(input())
        # k = 2
        root = KdNode()
        root = createKDTree(root, data)
        k_nearest_point = findKNearest(root, target, k)[-k:]
        # print(k_nearest_point)
        results.append(k_nearest_point)
    result_str = ''
    for k_nearest_point in results:
        for x in k_nearest_point[::-1]:
            result_str += " ".join([f2s(y) for y in list(x[0])]) + ","
        result_str = result_str[0:len(result_str)-1]
        result_str += "\n"
    print(result_str[0:len(result_str) - 1])
