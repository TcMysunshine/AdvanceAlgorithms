#!/usr/bin/env python
# coding=utf-8

# @file dfs.py
# @brief dfs
# @author Anemone95,x565178035@126.com
# @version 1.0
# @date 2019-02-25 14:49

book = set()
max_depth = -1


def dfs(graph, start, depth):
    global book
    global max_depth
    if depth > max_depth:
        max_depth = depth
    for e in graph[start]:
        if e not in book:
            book.add(e)
            dfs(graph, e, depth + 1)
            book.remove(e)


if __name__ == '__main__':
    test_num = input()
    results = []
    for k in range(int(test_num)):
        book = set()
        max_depth = -1
        point_num, start = input().split()
        point_labels = input().split()
        graph = {}
        for i in point_labels:
            graph[i] = []

        for i in range(int(point_num)):
            inpt = input().split()
            for j in range(int(point_num)):
                if inpt[1 + j] != '0':
                    graph[inpt[0]].append(point_labels[j])
        print(graph)
        book.add(start)
        dfs(graph, start, 1)
        results.append(max_depth)
    for x in results:
        print(x)
