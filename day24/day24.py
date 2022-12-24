with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

with open("expected.txt", "r") as f:
    expected = f.read().split("\n\n")
    f.close()


# test cases based on example
def check_states(grid):
    generator = generate_moves(grid)

    for i in range(len(expected)):
        if not save_state(next(generator)) == expected[i]:
            return False
    return True


EMPTY = 1
UP = 2
DOWN = 3
LEFT = 5
RIGHT = 7
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def save_state(grid):
    out = ""
    for line in grid:
        for num in line:
            if num == 0:
                out += "#"
            elif num == 1:
                out += "."
            elif num == UP:
                out += "^"
            elif num == DOWN:
                out += "v"
            elif num == LEFT:
                out += "<"
            elif num == RIGHT:
                out += ">"
            elif num == -1:
                out += "E"
            else:
                x = [direction for direction in DIRECTIONS if num % direction == 0]
                out += str(len(x))

        out += "\n"
    return out.strip()

def print_grid(grid):
    print(save_state(grid))

def make_step(grid):
    out = [[1 for _ in range(len(grid[1]))] for _ in range(len(grid))]

    for i, line in enumerate(grid):
        for j, num in enumerate(line):
            #  generate walls
            if num == 0:
                out[i][j] = 0

    for i, line in enumerate(grid):
        for j, num in enumerate(line):
            if num != 0:
            # Blizzard moving directions
                if num % UP == 0:
                    if out[i-1][j] != 0:
                        out[i-1][j] *= UP
                    # reached edge
                    else:
                        out[-2][j] *= UP
                if num % DOWN == 0:
                    if out[i+1][j] != 0:
                        out[i+1][j] *= DOWN
                    else:
                        out[1][j] *= DOWN
                if num % LEFT == 0:
                    if out[i][j-1] != 0:
                        out[i][j-1] *= LEFT
                    else:
                        out[i][-2] *= LEFT
                if num % RIGHT == 0:
                    if out[i][j+1] != 0:
                        out[i][j+1] *= RIGHT
                    else: 
                        out[i][1] *= RIGHT
    return out

def generate_moves(grid):
    yield grid
    while True:
        grid = make_step(grid)
        yield grid

def is_valid_square(grid, row, col):
    if row < 0 or col < 0 or row + 1 > len(grid) or col+1 > len(grid[0]):
        return False
    return grid[row][col] == 1

def BFS(grid, generator, states, s_row, s_col, g_row, g_col):
    move_map = [(1,0), (0,1), (0,0), (-1, 0), (0, -1)]
    # generator = generate_moves(grid)

    rows, cols = len(grid), len(grid[0])

    s_time = 0
    curr = (s_row, s_col, s_time)
    found = set()
    Q = []
    Q.append(curr)
    found.add(curr)

    while Q:
        v = Q.pop(0)
        row, col, time = v
        if row == g_row and col == g_col:
            return time

        if time+1 > len(states):
            states.append(next(generator))
        
        moves = [(row+move[0], col+move[1]) for move in move_map]
        legal_moves = [move for move in moves if is_valid_square(states[time], move[0], move[1])]
        for move in legal_moves:
            n_row, n_col, n_time = move[0], move[1], time + 1
            if (n_row,n_col, n_time) not in found:
                found.add((n_row,n_col, n_time))
                Q.append((n_row, n_col, n_time))

def part_one(data):
    grid = []
    for line in data:
        curr = []
        for char in line:
            if char == "#":
                curr.append(0)
            elif char == ".":
                curr.append(1)
            elif char == "^":
                curr.append(UP)
            elif char == "v":
                curr.append(DOWN)
            elif char == "<":
                curr.append(LEFT)
            elif char == ">":
                curr.append(RIGHT)
            else:
                assert False, "You shouldn't have reached this point"
        grid.append(curr)
    
    rows, cols = len(grid), len(grid[0])
    generator = generate_moves(grid)
    
    states = []
    start_row, start_col, end_row, end_col = 0, 1, rows-1, cols-2 
    next(generator)
    return BFS(grid, generator, states, start_row, start_col, end_row, end_col)
    

def part_two(data):
    grid = []
    for line in data:
        curr = []
        for char in line:
            if char == "#":
                curr.append(0)
            elif char == ".":
                curr.append(1)
            elif char == "^":
                curr.append(UP)
            elif char == "v":
                curr.append(DOWN)
            elif char == "<":
                curr.append(LEFT)
            elif char == ">":
                curr.append(RIGHT)
            else:
                assert False, "You shouldn't have reached this point"
        grid.append(curr)
    
    rows, cols = len(grid), len(grid[0])
    generator = generate_moves(grid)

    start_row, start_col, end_row, end_col = 0, 1, rows-1, cols-2 
    next(generator)
    states = [next(generator) for _ in range(1000)]
    there = BFS(grid, generator, states, start_row, start_col, end_row, end_col)
    back = BFS(grid, generator, states[there:], end_row, end_col, start_row, start_col)
    back_again = BFS(grid, generator, states[there+back:], start_row, start_col, end_row, end_col)
    print(there, back, back_again)
    return there + back + back_again


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

