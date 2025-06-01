bombs = [[False for y in range(10)] for x in range(10)]
bombs[0][1] = True
bombs[0][0] = True
bombs[1][1] = True
bombs[1][8] = True
bombs[4][4] = True
bombs[8][8] = True

def count_adjacent_bombs(x, y, bombs):
    count = 0
    for i in range(max(0, x - 1), min(len(bombs), x + 2)):
        for j in range(max(0, y - 1), min(len(bombs[0]), y + 2)):
            if bombs[i][j]:
                count += 1
    return count

for x in range(len(bombs)):
    for y in range(len(bombs[0])):
        if bombs[x][y]:
            print('*', end=' ')
        else:
            if count_adjacent_bombs(x, y, bombs) == 0:
                 print("#", end=' ')
            else:
                print("#", end=' ')
    print()
