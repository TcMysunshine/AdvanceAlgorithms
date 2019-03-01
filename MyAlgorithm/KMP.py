def findNext(p):
    length = len(p)
    next = []
    next.append(-1)
    for i in range(1, length):
        next.append(0)
    j = 0
    k = -1
    # 'aab'
    while j < length - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
    return next


def KMPMatch(s, p):
    next = findNext(p)
    i, j = 0,-1
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(p):
        return i - j
    else:
        return -1


if __name__ == '__main__':
    s = 'ababaaababaa'
    p = 'aabaab'
    next = findNext(p)
