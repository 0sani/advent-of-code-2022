import time

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

with open("smaller_test.txt", "r") as f:
    small = [line.strip() for line in f.readlines()]
    f.close()

with open("expected.txt", "r") as f:
    expected = f.read()
    f.close()

NO_MOVE = 0
NORTH = 2
SOUTH = 3
WEST = 5
EAST = 7

DIRECTIONS = [NORTH, SOUTH, WEST, EAST]

def direction_gen():
    while True:
        yield NORTH
        yield SOUTH
        yield WEST
        yield EAST


class Elf():
    elves = []
    start_direction = NO_MOVE


    def __init__(self, id, x, y, settled=False) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.ideal_x = x
        self.ideal_y = y 
        self.settled = settled
        self.elves.append(self)

    def get_direction(self):
        neighbors = get_neighbors(self.x, self.y)

        if neighbors == 1:
            return NO_MOVE

        # generate possible moves
        out = [0] * 4
        if neighbors % NORTH != 0:
            out[0] = NORTH
        if neighbors % SOUTH != 0:
            out[1] = SOUTH
        if neighbors % WEST != 0:
            out[2] = WEST
        if neighbors % EAST != 0:
            out[3] = EAST
        
        if sum(out) == 0:
            return NO_MOVE

        # return first according to search order
        if Elf.start_direction == NORTH:
            return [dir for dir in out if dir != 0][0]
        if Elf.start_direction == SOUTH:
            out.append(out.pop(0))
            return [dir for dir in out if dir != 0][0]
        if Elf.start_direction == WEST:
            out = out[2:] + out[:2]
            return [dir for dir in out if dir != 0][0]
        if Elf.start_direction == EAST:
            out = out[3:] + out[:3]
            return [dir for dir in out if dir != 0][0]
        
        assert False, "You should not have reached this point"
    
    def trial_move(self):
        direction = self.get_direction()
        if direction == NO_MOVE:
            pass
        elif direction == NORTH:
            self.ideal_y += 1
        elif direction == SOUTH:
            self.ideal_y -= 1
        elif direction == WEST:
            self.ideal_x -= 1
        elif direction == EAST:
            self.ideal_x += 1
        else:
            assert False, "You should not have reached this point, invalid direction"
        return (self.ideal_x, self.ideal_y)

    def __str__(self) -> str:
        return f"Elf(ID: {self.id} Pos: ({self.x}, {self.y}) Settled: {self.settled})"

    def __repr__(self) -> str:
        return str(self)


def get_neighbors(x, y):
    # 10  2 14
    # 5  X 7
    # 15 3 21
    neighbors = 1
    for elf in Elf.elves:
        if x-1 <= elf.x <= x+1 and elf.y == y + 1:
            neighbors *= NORTH
        if x-1 <= elf.x <= x+1 and elf.y == y - 1:
            neighbors *= SOUTH
        if elf.x == x - 1 and y-1 <= elf.y <= y+1:
            neighbors *= WEST
        if elf.x == x + 1 and y-1 <= elf.y <= y+1:
            neighbors *= EAST
    return neighbors

def get_dimensions():
    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")

    for elf in Elf.elves:
        min_x = min(elf.x, min_x)
        max_x = max(elf.x, max_x)
        min_y = min(elf.y, min_y)
        max_y = max(elf.y, max_y)
    return (min_x, max_x, min_y, max_y)

def print_elves(min_x, max_x, min_y, max_y):
    print(save_state(min_x, max_x, min_y, max_y))

def print_debug():
    x1,x2,y1,y2 = get_dimensions()
    # print("Direction: ", Elf.start_direction)
    # print("\n".join([str(elf) for elf in Elf.elves]))
    print_elves(x1,x2,y1,y2)
    print(x1,x2,y1,y2)
    print("")

def save_state(min_x, max_x, min_y, max_y):
    out = ""
    for i in range(max_y,min_y-1, -1):
        for j in range(min_x, max_x+1):
            found = False
            for elf in Elf.elves:
                if (elf.x == j and elf.y == i):
                    out += "#"
                    found = True
                    break
            if not found:
                out += "."
        out += "\n"
    return out.strip()

def part_one(data):
    gen = direction_gen()
    count = 0
    for i, line in enumerate(reversed(data)):
        for j, char in enumerate(line):
            if char == "#":
                Elf(count, j,i, False)
                count += 1

    for i in range(10):
        print(f"Starting iteration: {i}")
        # sets the starting direction
        Elf.start_direction = next(gen)
        

        candidate_moves = {}
        # gets all trial moves:
        for elf in Elf.elves:
            move = elf.trial_move()
            # no move
            if move == (elf.x, elf.y):
                elf.settled = True
            else:
                if move not in candidate_moves:
                    candidate_moves[move] = [elf]
                else:
                    candidate_moves[move].append(elf)

        # makes moves
        for move in candidate_moves:
            if len(candidate_moves[move]) == 1:
                elf = candidate_moves[move][0]

                elf.x = elf.ideal_x
                elf.y = elf.ideal_y
            else:
                for elf in candidate_moves[move]:
                    elf.ideal_x = elf.x
                    elf.ideal_y = elf.y
    
    
    x1,x2,y1,y2 = get_dimensions()
    return (x2-x1+1) * (y2-y1+1) - len(Elf.elves)

def part_two(data):
    gen = direction_gen()
    count = 0
    for i, line in enumerate(reversed(data)):
        for j, char in enumerate(line):
            if char == "#":
                Elf(count, j,i, False)
                count += 1

    iters = 0
    while not all([elf.settled for elf in Elf.elves]):
        print(f"Starting iteration: {iters}")
        # sets the starting direction
        Elf.start_direction = next(gen)
        

        candidate_moves = {}
        # gets all trial moves:
        for elf in Elf.elves:
            move = elf.trial_move()
            if move == (elf.x, elf.y):
                elf.settled = True
            else:
                elf.settled = False
                if move not in candidate_moves:
                    candidate_moves[move] = [elf]
                else:
                    candidate_moves[move].append(elf)

        # makes moves
        for move in candidate_moves:
            if len(candidate_moves[move]) == 1:
                elf = candidate_moves[move][0]

                elf.x = elf.ideal_x
                elf.y = elf.ideal_y
            else:
                for elf in candidate_moves[move]:
                    elf.ideal_x = elf.x
                    elf.ideal_y = elf.y
        iters += 1
    return iters





def main():
    print("Part One: ")
    # print("Test:", part_one(test))
    # print("Smaller Test:", part_one(small))
    # print("Result:", part_one(data))
    print("\nPart Two: ")
    # print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()