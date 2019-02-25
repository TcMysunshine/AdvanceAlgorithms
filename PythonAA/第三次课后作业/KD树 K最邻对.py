import numpy as np
from numpy import array
import math

class decisionnode:
    def __init__(self, value=None, col=None, rb=None, lb=None):
        self.value = value
        self.col = col
        self.rb = rb
        self.lb = lb


# 读取数据并将数据转换为矩阵形式
def readdata(filename):
    data = open(filename).readlines()
    x = []
    for line in data:
        line = line.strip().split('\t')
        x_i = []
        for num in line:
            num = float(num)
            x_i.append(num)
        x.append(x_i)
    x = array(x)
    return x


# 求序列的中值
def median(x):
    n = len(x)
    x = list(x)
    x_order = sorted(x)
    return x_order[n // 2], x.index(x_order[n // 2])


# 以j列的中值划分数据，左小右大，j=节点深度%列数
def buildtree(x, j=0):
    rb = []
    lb = []
    m, n = x.shape
    if m == 0: return None
    edge, row = median(x[:, j].copy())
    for i in range(m):
        if x[i][j] > edge:
            rb.append(i)
        if x[i][j] < edge:
            lb.append(i)
    rb_x = x[rb, :]
    lb_x = x[lb, :]
    rightBranch = buildtree(rb_x, (j + 1) % n)
    leftBranch = buildtree(lb_x, (j + 1) % n)
    return decisionnode(x[row, :], j, rightBranch, leftBranch)


# 搜索树：输出目标点的近邻点
def traveltree(node, aim):
    global pointlist  # 存储排序后的k近邻点和对应距离
    if node == None: return
    col = node.col #进行分割的轴
    if aim[col] > node.value[col]:
        traveltree(node.rb, aim)
    if aim[col] < node.value[col]:
        traveltree(node.lb, aim)
    dis = dist(node.value, aim) #找到分割的点
    if len(knears) < k:
        knears.setdefault(tuple(node.value.tolist()), dis)  # 列表不能作为字典的键
        pointlist = sorted(knears.items(), key=lambda item: item[1], reverse=True)#按照距离排序
    elif dis <= pointlist[0][1]:
        knears.setdefault(tuple(node.value.tolist()), dis)
        pointlist = sorted(knears.items(), key=lambda item: item[1], reverse=True)
    if node.rb != None or node.lb != None:
        if abs(aim[node.col] - node.value[node.col]) < pointlist[0][1]:
            if aim[node.col] < node.value[node.col]:
                traveltree(node.rb, aim)
            if aim[node.col] > node.value[node.col]:
                traveltree(node.lb, aim)
    return pointlist


def dist(x1, x2):  # 欧式距离的计算
    # return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(x1, x2)))
    return ((np.array(x1) - np.array(x2)) ** 2).sum() ** 0.5


knears = {}
k = int(input('请输入k的值'))
if k < 2: print('k不能是1')
global pointlist
pointlist = []
data =array([
    [3, 5],
    [6, 2],
    [5, 8],
    [9, 3],
    [8, 6],
    [1, 1],
    [2, 9]
])
# file = input('请输入数据文2件地址')
# data = readdata(file)
tree = buildtree(data)
tmp = [8.2, 4.6]
print(dist(tmp,[8,6]))
# tmp = input('请输入目标点')
# tmp = tmp.split(',')
aim = []
for num in tmp:
    num = float(num)
    aim.append(num)
aim = tuple(aim)
pointlist = traveltree(tree, aim)
for point in pointlist[:k]:
    print(point)
