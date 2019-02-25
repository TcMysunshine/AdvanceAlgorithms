def main():
    # a = [int(x) for x in input().split()]
    # b = [int(x) for x in input().split()]
    a = [100, 20, 98, 1, 2, 3]
    b = [1, 2, 3, 4, 5, 45]
    suma = sum(a)
    sumb = sum(b)
    min = dfs(a, b, suma, sumb)
    print(min)


def dfs(a, b, suma,sumb):
    diff = suma-sumb
    best_change, ni, nj = 0, 0, 0
    for i in range(len(a)):
        for j in range(len(b)):
            d = a[i] - b[j]
            if abs(diff - 2 * d) < abs(diff - 2 * best_change):
                ni, nj = i, j
                best_change = d

    if 0 == best_change:
        return diff
    temp = a[ni]
    a[ni] = b[nj]
    b[nj] = temp
    return dfs(a, b, suma - best_change, sumb + best_change)


if __name__ == '__main__':
    main()