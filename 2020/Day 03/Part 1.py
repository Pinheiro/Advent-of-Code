grid = [[char for char in line] for line in open("2020/Day 03/Input.txt").read().splitlines()]
map = [[char for char in line] for line in open("2020/Day 03/Input.txt").read().splitlines()]

x = 0
y = 0

bottom = len(map) - 1
while True:
    x += 3
    y += 1
    if (x + 1 > len(map[0])):
        for i in range(len(map)):
            map[i].extend(grid[i])
    if map[y][x] == '.':
        map[y][x] = 'O'
    if map[y][x] == '#':
        map[y][x] = 'X'
    if y == bottom:
        break

print(sum([row.count('X') for row in map]))