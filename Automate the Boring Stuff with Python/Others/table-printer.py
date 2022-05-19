tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    # Store the maximum width of each column as a list of integers.
    col_widths = [0] * len(table)

    # 获取每一个 list 里最长的 string 的 length，储存到 col_width 这个 list 里
    for innerList in table:
        maxStrLen = 0
        for word in innerList:
            if len(word) > maxStrLen:
                maxStrLen = len(word)
            else:
                pass
        col_widths[table.index(innerList)] = maxStrLen

    # table list 的 y 轴就是最终 table 的 x 轴。
    # 我们希望先保持 table list 的 x 轴不变, print 出 table list 的 y 轴。
    # 那么把 x 轴写在外层 loop 就行了。
    for x in range(len(table[0])):  # 此处的 x 是 table list 的 x 轴
        for y in range(len(table)):  # 此处的 y 是 table list 的 y 轴
            if y < len(col_widths) - 1:
                print(table[y][x].rjust(col_widths[y], ' '), end=' ')
            else:
                print(table[y][x].rjust(col_widths[y], ' '))


print_table(tableData)