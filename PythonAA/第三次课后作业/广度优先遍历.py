
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
            for j in range(self.nodesNum):
                if self.arr[v][j] == 1 and j not in visited:
                    queue.append(j)
                    visited.append(j)
                    bfsResults.append(self.nodes[j])
        return bfsResults


if __name__ == '__main__':
    # nodes = ['a', 'b', 'c', 'd']
    # root = 'a'
    # nodesNum = 4
    # arr = [
    #      [0, 1, 1, 0],
    #      [1, 0, 1, 0],
    #      [1, 1, 0, 1],
    #      [0, 0, 1, 0]
    # ]
    # print(nodes.index(root))
    num = int(input())
    results = ""
    for i in range(num):
        resultStr=""
        arr1 = input().split(" ")
        nodesNum = int(arr1[0])
        root = arr1[1]
        nodes = input().split(" ")
        rootIndex = nodes.index(root)
        neighMat = []
        for j in range(nodesNum):
            arr2=[int(x) for x in input().split()[1:]]
            neighMat.append(arr2)
        # print(neighMat)
        # print(nodes)
        # print(nodesNum)
        g = Graph(nodes, nodesNum, neighMat)
        results += " ".join(g.BFS(root))+"\n"
    print(results[:len(results)-1])
    # g = Graph(nodes, nodesNum, arr)
    # print(" ".join(g.BFS(root)))
    # print(g.DFS(root))