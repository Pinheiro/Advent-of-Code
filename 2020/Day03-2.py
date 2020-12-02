import copy
grid = [[char for char in line] for line in open("2020/Day03.Input").read().splitlines()]

def trees(dx, dy):
    map = copy.deepcopy(grid)
    x = 0
    y = 0
    bottom = len(map) - 1
    while True:
        x += dx
        y += dy
        if ((x + 1) > len(map[0])):
            for i in range(len(map)):
                map[i].extend(grid[i])
        if map[y][x] == '.':
            map[y][x] = 'O'
        if map[y][x] == '#':
            map[y][x] = 'X'
        if y == bottom:
            break
    return sum([row.count('X') for row in map])

print(trees(1, 1) * trees(3, 1) * trees(5, 1) * trees(7, 1) * trees(1, 2))