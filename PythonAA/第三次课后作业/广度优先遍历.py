
class Graph():
    def __init__(self, nodes, nodesNum, arr):
        self.nodes = nodes
        self.root = root
        self.nodesNum = nodesNum
        self.arr = arr

    def BFS(self, root):
        bfsResults = []
        visited = []
        queue = []
        rootIndex = self.nodes.index(root)
        visited.append(rootIndex)
        queue.append(rootIndex)
        bfsResults.append(root)
        while queue:
            v = queue.pop(0)
            for j in range(nodesNum):
                if self.arr[v][j] == 1 and j not in visited:
                    queue.append(j)
                    visited.append(j)
                    bfsResults.append(self.nodes[j])
        return bfsResults


if __name__ == '__main__':
    nodes = ['a', 'b', 'c', 'd']
    root = 'a'
    nodesNum = 4
    arr = [
         [0, 1, 1, 0],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [0, 0, 1, 0]
    ]
    # nodes = ['0', '1', '2', '3','4']
    # root = '1'
    # nodesNum = 5
    # arr = [
    #     [0, 1, 0, 1, 0],
    #     [1, 0, 1, 0, 0],
    #     [0, 1, 0, 1, 1],
    #     [1, 0, 1, 0, 1],
    #     [0, 0, 1, 1, 0]
    # ]

    g = Graph(nodes, nodesNum, arr)
    print(" ".join(g.BFS(root)))
    # print(g.DFS(root))