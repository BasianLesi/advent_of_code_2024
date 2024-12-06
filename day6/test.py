with open('input') as file:
    input = [[*x] for x in file.read().strip().splitlines()]

h = len(input)
w = len(input[0])
start = next(
    (i, j) for i, row in enumerate(input)
    for j, element in enumerate(row) if element == '^'
)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1(grid):
    visited = {start}
    dir = 0
    prev = start

    while True:
        dy, dx = dirs[dir]
        next = (prev[0] + dy, prev[1] + dx)

        if next[0] < 0 or next[1] < 0 or next[0] >= h or next[1] >= w:
            break

        val = grid[next[0]][next[1]]

        if val == '#':
            dir = (dir + 1) % len(dirs)
        else:
            visited.add(next)
            prev = next

    return len(visited)

def does_loop(grid):
    steps = set()
    dir = 0
    prev = start

    while True:
        dy, dx = dirs[dir]
        next = (prev[0] + dy, prev[1] + dx)

        if next[0] < 0 or next[1] < 0 or next[0] >= h or next[1] >= w:
            break

        val = grid[next[0]][next[1]]

        if val == '#':
            dir = (dir + 1) % len(dirs)
        elif prev + next in steps:
            return True
        else:
            steps.add(prev + next)
            prev = next

    return False


def part2(input):
    loops = 0

    for y in range(len(input)):
        for x in range(len(input[0])):
            val = input[y][x]
            
            if val != '.':
                continue

            changed = (y, x, val)
            input[y][x] = '#'

            if does_loop(input):
                loops += 1

            input[y][x] = val

    return loops


print(part1(input))
print(part2(input))
