chessBoard = {'1h': 'bking', '8c': 'wqueen', '8g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

board = {'1a': 'bking', '2a': 'bqueen', '3a': 'brook', '4a': 'brook',
         '5a': 'bknight', '6a': 'bknight', '7a': 'bbishop', '8a': 'bbishop',
         '1b': 'bpawn', '2b': 'bpawn', '3b': 'bpawn', '4b': 'bpawn',
         '5b': 'bpawn', '6b': 'bpawn', '7b': 'bpawn', '8b': 'bpawn',
         '1c': 'wking', '2c': 'wqueen', '3c': 'wrook', '4c': 'wrook',
         '5c': 'wbishop', '6c': 'wbishop', '7c': 'wknight', '8c': 'wknight',
         '1e': 'wpawn', '2e': 'wpawn', '3e': 'wpawn', '4e': 'wpawn',
         '5e': 'wpawn', '6e': 'wpawn', '7e': 'wpawn', '8e': 'wpawn',
         '1f': '', '2f': '', '3f': '', '4f': '', '5f': '', '6f': '', '7f': '', '8f': '',
         '1g': '', '2g': '', '3g': '', '4g': '', '5g': '', '6g': '', '7g': '', '8g': '',
         '1h': '', '2h': '', '3h': '', '4h': '', '5h': '', '6h': '', '7h': '', '8e': '', }


def isValidChessBoard(chessB):
    # variables
    bking_cnt = 0
    bqueen_cnt = 0
    brook_cnt = 0
    bbishop_cnt = 0
    bknight_cnt = 0
    bpawn_cnt = 0

    wking_cnt = 0
    wqueen_cnt = 0
    wrook_cnt = 0
    wbishop_cnt = 0
    wknight_cnt = 0
    wpawn_cnt = 0

    # 先遍历给定的这个 chessboard 计算每个棋子出现的个数，存到各个 variable 中待之后做进一步调用。
    for k, v in chessB.items():
        if v == 'bking':
            bking_cnt += 1
        if v == 'bqueen':
            bqueen_cnt += 1
        if v == 'brook':
            brook_cnt += 1
        if v == 'bbishop':
            bbishop_cnt += 1
        if v == 'bknight':
            bknight_cnt += 1
        if v == 'bpawn':
            bpawn_cnt += 1

        if v == 'wking':
            wking_cnt += 1
        if v == 'wqueen':
            wqueen_cnt += 1
        if v == 'wrook':
            wrook_cnt += 1
        if v == 'wbishop':
            wbishop_cnt += 1
        if v == 'wknight':
            wknight_cnt += 1
        if v == 'wpawn':
            wpawn_cnt += 1

        # 开始正式检查之前，先 check 每个棋子位置的代号（数字+字母 a-h）是否符合要求。
        if int(k[0]) > 8:
            return False
        elif k[1] != 'a' and k[1] != 'b' and k[1] != 'c' and k[1] != 'd' and k[1] != 'e' and k[1] != 'f' and k[
            1] != 'g' and \
                k[1] != 'h':
            return False

    # 现在分别 check 各个棋子角色的数量是否符合要求。
    if bking_cnt > 1 or wking_cnt > 1:
        return False
    elif bqueen_cnt > 1 or wqueen_cnt > 1:
        return False
    elif brook_cnt > 2 or wrook_cnt > 2:
        return False
    elif bbishop_cnt > 2 or wbishop_cnt > 2:
        return False
    elif bknight_cnt > 2 or wknight_cnt > 2:
        return False
    elif bpawn_cnt > 8 or wpawn_cnt > 8:
        return False

    # 这里 check 各边棋子的总量的是否小于 16 个。
    if bking_cnt + bqueen_cnt + brook_cnt + bknight_cnt + bpawn_cnt > 16:
        return False
    elif wking_cnt + wqueen_cnt + wrook_cnt + wknight_cnt + wpawn_cnt > 16:
        return False

    return True


print(isValidChessBoard(board))
