chessBoard = {'1h': 'bking', '6c': 'wqueen', '8g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

# variables
bkingCount = 0
bqueenCount = 0
brookCount = 0
bbishopCount = 0
bknightCount = 0
bpawnCount = 0

wkingCount = 0
wqueenCount = 0
wrookCount = 0
wbishopCount = 0
wknightCount = 0
wpawnCount = 0

for k, v in chessBoard.items():
    if v == 'bking':
        bkingCount += 1
    if v == 'bqueen':
        bqueenCount += 1
    if v == 'brook':
        brookCount += 1
    if v == 'bbishop':
        bbishopCount += 1
    if v == 'bknight':
        bknightCount += 1
    if v == 'bpawn':
        bpawnCount += 1

    if v == 'wking':
        wkingCount += 1
    if v == 'wqueen':
        wqueenCount += 1
    if v == 'wrook':
        wrookCount += 1
    if v == 'wbishop':
        wbishopCount += 1
    if v == 'wknight':
        wknightCount += 1
    if v == 'wpawn':
        wpawnCount += 1

    if int(k[0]) > 8:
        print("failed, key > 8")
        break
    elif k[1] != 'a' and k[1] != 'b' and k[1] != 'c' and k[1] != 'd' and k[1] != 'e' and k[1] != 'f' and k[
        1] != 'g' and \
            k[1] != 'h':
        print("failed, key's abcd != ..")
        break

if bkingCount > 1 or wkingCount > 1:
    print("failed, Count")
elif bqueenCount > 1 or wqueenCount > 1:
    print("failed, Count")
elif brookCount > 2 or wrookCount > 2:
    print("failed, Count")
elif bbishopCount > 2 or wbishopCount > 2:
    print("failed, Count")
elif bknightCount > 2 or wknightCount > 2:
    print("failed, Count")
elif bpawnCount > 8 or wpawnCount > 8:
    print("failed, Count")
else:
    pass

if bkingCount + bqueenCount + brookCount + bknightCount + bpawnCount > 16:
    print("failed, all count")
elif wkingCount + wqueenCount + wrookCount + wknightCount + wpawnCount > 16:
    print("failed, all count")
