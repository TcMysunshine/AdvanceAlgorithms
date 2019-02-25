# tr左上角行号，tc左上角列号。dr特殊方格行号，dc特殊方格列号

def chessboard(board, size, tr, tc, dr, dc):
    if size <= 1:
        return
    global tile
    tile += 1
    current_tile = tile
    size //= 2
    if dr < tr + size and dc < tc + size:
        chessboard(board, size, tr, tc, dr, dc)
    else:
        board[tr + size - 1][tc + size - 1] = current_tile
        chessboard(board, size, tr, tc, tr + size - 1, tc + size - 1)

    if dr >= tr + size and dc < tc + size:
        chessboard(board, size, tr + size, tc, dr, dc)
    else:
        board[tr + size][tc + size - 1] = current_tile
        chessboard(board, size, tr + size, tc,
                   tr + size, tc + size - 1)

    if dr < tr + size and dc >= tc + size:
        chessboard(board, size, tr, tc + size, dr, dc)
    else:
        board[tr + size - 1][tc + size] = current_tile
        chessboard(board, size, tr, tc + size,
                   tr + size - 1, tc + size)

    if dr >= tr + size and dc >= tc + size:
        chessboard(board, size, tr + size, tc + size, dr, dc)
    else:
        board[tr + size][tc + size] = current_tile
        chessboard(board, size, tr + size, tc + size,
                   tr + size, tc + size)


if __name__ == '__main__':
    tile = 0
    num = int(input())
    resultList=[]
    for i in range(num):
        arr1 = [int(x) for x in input().split(" ")]
        chessboard_size = pow(2, arr1[0])
        board = [[0 for x in range(chessboard_size)] for y in range(chessboard_size)]
        chessboard(board, chessboard_size, 0, 0, arr1[1], arr1[2])
        arr2 = [int(x) for x in input().split(" ")]
        label = board[arr2[0]][arr2[1]]
        resultstr = ''
        for i in range(chessboard_size):
            for j in range(chessboard_size):
                if i == arr2[0] and j == arr2[1]:
                    continue
                else:
                    if board[i][j] == label:
                        resultstr += str(i) + " " + str(j) + ","
        resultList.append(resultstr[:-1])
    for result in resultList:
        print(result)
