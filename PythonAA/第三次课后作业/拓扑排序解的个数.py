def TopologicalSort(matrix, nodes):
    if not nodes:
        return 1
    next_list = []
    # 把所有入度为0的点加入列表
    for node in nodes:
        in_degree = 0
        j = nodes[node]
        for node_name in nodes:
            i = nodes[node_name]
            if matrix[i][j] == 1:
                in_degree += 1
        if in_degree == 0:
            next_list.append(node)
    if not next_list:
        return 0
    total = 0

    for node in next_list:
        new_nodes = nodes.copy()
        del (new_nodes[node])
        total += TopologicalSort(matrix, new_nodes)
    return total


if __name__ == "__main__":
    case_num = int(input())
    results = []
    for _ in range(case_num):
        edges = list(map(lambda x: (x.split(' ')), input().split(',')))
        # 每一个节点的索引值
        nodes = {}
        count = 0
        for edge in edges:
            for i in edge:
                if i not in nodes:
                    nodes[i] = count
                    count += 1
        matrix = [[0] * len(nodes) for _ in nodes]
        for edge in edges:
            src, tar = edge
            src, tar = nodes[src], nodes[tar]
            matrix[src][tar] = 1
        res = TopologicalSort(matrix, nodes)
        results.append(res)
    for x in results:
        print(x)