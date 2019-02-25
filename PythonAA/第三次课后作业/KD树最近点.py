from math import sqrt
from collections import namedtuple


# kd-tree每个结点中主要包含的数据结构如下
class KdNode(object):
    def __init__(self, dom_elt=None, split=None, left=None, right=None):
        self.dom_elt = dom_elt  # k维向量节点(k维空间中的一个样本点)
        self.split = split  # 整数（进行分割维度的序号）
        self.left = left  # 该结点分割超平面左子空间构成的kd-tree
        self.right = right  # 该结点分割超平面右子空间构成的kd-tree


class KdTree(object):
    def __init__(self, data):

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

        # def CreateNode(split, data_set):  # 按第split维划分数据集exset创建KdNode
        #     if not data_set:  # 数据集为空
        #         return None
        #     # key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较
        #     # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为需要获取的数据在对象中的序号
        #     # data_set.sort(key=itemgetter(split)) # 按要进行分割的那一维数据排序
        #     data_set.sort(key=lambda x: x[split])
        #     split_pos = len(data_set) // 2  # //为Python中的整数除法
        #     median = data_set[split_pos]  # 中位数分割点
        #     split_next = (split + 1) % k  # cycle coordinates
        #
        #     # 递归的创建kd树
        #     return KdNode(median, split,
        #                   CreateNode(split_next, data_set[:split_pos]),  # 创建左子树
        #                   CreateNode(split_next, data_set[split_pos + 1:]))  # 创建右子树
        root = KdNode()
        self.root = createKDTree(root, data)  # 从第0维分量开始构建kd树,返回根节点


# KDTree的前序遍历
def preorder(root):
    print(root.dom_elt)
    if root.left:  # 节点不为空
        preorder(root.left)
    if root.right:
        preorder(root.right)


result = namedtuple("Result_tuple", "nearest_point  nearest_dist  nodes_visited")
resultsList = []


def find_nearest(tree, point):
    k = len(point)  # 数据维度

    def travel(kd_node, target, max_dist):
        if kd_node is None:
            return result([0] * k, float("inf"), 0)  # python中用float("inf")和float("-inf")表示正负无穷

        nodes_visited = 1

        s = kd_node.split  # 进行分割的维度
        pivot = kd_node.dom_elt  # 进行分割的“轴”

        if target[s] <= pivot[s]:  # 如果目标点第s维小于分割轴的对应值(目标离左子树更近)
            nearer_node = kd_node.left  # 下一个访问节点为左子树根节点
            further_node = kd_node.right  # 同时记录下右子树
        else:  # 目标离右子树更近
            nearer_node = kd_node.right  # 下一个访问节点为右子树根节点
            further_node = kd_node.left

        temp1 = travel(nearer_node, target, max_dist)  # 进行遍历找到包含目标点的区域

        nearest = temp1.nearest_point  # 以此叶结点作为“当前最近点”
        dist = temp1.nearest_dist  # 更新最近距离

        nodes_visited += temp1.nodes_visited

        if dist < max_dist:
            max_dist = dist  # 最近点将在以目标点为球心，max_dist为半径的超球体内

        temp_dist = abs(pivot[s] - target[s])  # 第s维上目标点与分割超平面的距离
        # resultsList.append(result(nearest, dist, nodes_visited))
        if max_dist < temp_dist:  # 判断超球体是否与超平面相交
            return result(nearest, dist, nodes_visited)  # 不相交则可以直接返回，不用继续判断

        # ----------------------------------------------------------------------
        # 计算目标点与分割点的欧氏距离
        temp_dist = sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(pivot, target)))

        if temp_dist < dist:  # 如果“更近”
            nearest = pivot  # 更新最近点
            dist = temp_dist  # 更新最近距离
            max_dist = dist  # 更新超球体半径

        # 检查另一个子结点对应的区域是否有更近的点
        temp2 = travel(further_node, target, max_dist)

        nodes_visited += temp2.nodes_visited
        if temp2.nearest_dist < dist:  # 如果另一个子结点内存在更近距离
            nearest = temp2.nearest_point  # 更新最近点
            dist = temp2.nearest_dist  # 更新最近距离
        return result(nearest, dist, nodes_visited)

    return travel(tree.root, point, float("inf"))  # 从根节点开始递归


if __name__ == "__main__":
    data = [
        [3, 5],
        [6, 2],
        [5, 8],
        [9, 3],
        [8, 6],
        [1, 1],
        [2, 9]
    ]
    kd = KdTree(data)
    ret = find_nearest(kd, [8.2, 4.6])

    print(ret)
    # print(float("inf"))
    for x in resultsList:
        print(x)
