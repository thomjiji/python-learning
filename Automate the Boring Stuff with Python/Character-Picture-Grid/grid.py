grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '*', '*', '.', '.', '.'],
        ['*', '*', '*', '*', '.', '.'],
        ['*', '*', '*', '*', '*', '.'],
        ['.', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '.'],
        ['*', '*', '*', '*', '.', '.'],
        ['.', '*', '*', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# main loop
# 把 grid 这个 list 的 x，y 轴调换，x 作为最终图形的 y 轴，y 作为最终图形的 x 轴。
# 这里两个 loop 的 x，y 可以理解为最终图形的 y 和 x 轴。
# for x in range(6):
#     for y in range(9):
#         if y < 8:
#             print(grid[y][x], end='')
#         else:
#             print(grid[y][x])

# 把 grid 这个 list 的 x，y 轴调换，x 作为最终图形的 y 轴，y 作为最终图形的 x 轴。
# 这里两个 loop 的 x，y 可以理解为最终图形的 x 和 y 轴。
for y in range(6):
    for x in range(9):
        if x < 8:
            print(grid[x][y],
                  end='')
        else:
            print(grid[x][y])

# 把 grid 这个 list 照样 print 出来，grid 的 x， y 就是最终图形的 x 轴和 y 轴。
# for y in range(9):
#     for x in range(6):
#         if x < 5:
#             print(grid[y][x],
#                   end='')
#         else:
#             print(grid[y][x])
