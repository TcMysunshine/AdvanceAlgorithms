def dfs(graph, root, depth):
    global max_depth
    global visited
    if depth > max_depth:
        max_depth = depth

    for x in graph[root]:
        if x not in visited:
            visited.append(x)
            dfs(graph, x, depth + 1)
            visited.pop()


if __name__ == '__main__':
    num = int(input())
    visited = []
    max_depth = -1
    results = []
    for _ in range(num):
        vertexNum, root = input().split(' ')
        graph = {}
        nodes = input().split(' ')
        for node in nodes:
            graph[node] = []
        for i in range(int(vertexNum)):
            line = input().split()
            for j in range(int(vertexNum)):
                if line[j + 1] == '1':
                    graph[line[0]].append(nodes[j])

        visited.append(root)
        dfs(graph, root, 1)
        results.append(max_depth)
    for x in results:
        print(x)
