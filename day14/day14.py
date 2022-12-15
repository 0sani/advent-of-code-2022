with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def parse(data, min_x, max_x, min_y, max_y, buffer):
    data = [[[int(num) for num in cord.split(",")] for cord in line.split(" -> ")] for line in data]


    # create grid
    grid = [[0 for i in range(max_x-min_x+1+ 2*buffer)] for j in range(max_y+3)]
    for shape in data:
        for i in range(len(shape)-1):
            a, b = shape[i], shape[i+1]
            x1, y1 = a[0]-min_x+buffer, a[1]
            x2, y2 = b[0]-min_x+buffer, b[1]
            if x1 == x2:
                for j in range(min(y1,y2), max(y1,y2)+1):
                    grid[j][x1] = 1
            else:
                for j in range(min(x1,x2), max(x1,x2)+1):
                    grid[y1][j] = 1

    return grid

def print_grid(grid):
    for line in grid:
        for num in line:
            if num == 0:
                print(".",end="")
            elif num == 1:
                print("#", end="")
            else:
                print("o", end="")
        print("")

def drop(grid, x, y):
    if grid[y][x] == 2:
        return False
    if x < 0 or x > len(grid[0]):
        return False
    if y > len(grid)-2:
        return False
    
    # print(x, y, len(grid))
    if grid[y+1][x] == 0:
        return drop(grid, x, y+1)
    else:
        if grid[y+1][x-1] == 0:
            return drop(grid, x-1, y+1)
        elif grid[y+1][x+1] == 0:
            return drop(grid, x+1, y+1)
        else:
            grid[y][x] = 2
            return True

def part_one(data, sub):
    if sub == "test":
        min_x = 494
        max_x = 503
        min_y = 4
        max_y = 9
        buffer = 1
    else:
        min_x = 448
        max_x = 514
        min_y = 13
        max_y = 180
        buffer = 1

    grid = parse(data, min_x,max_x,min_y,max_y, buffer)
    

    sand_origin = (500,0)
    count = 0
    while drop(grid, sand_origin[0]-min_x+1, sand_origin[1]):
        count += 1

    # print_grid(grid)
    return count



def part_two(data,sub):
    if sub == "test":
        min_x = 494
        max_x = 503
        min_y = 4
        max_y = 9
        buffer = 10
    else:
        min_x = 448
        max_x = 514
        min_y = 13
        max_y = 180
        buffer = 180

    grid = parse(data, min_x,max_x,min_y,max_y, buffer)

    for i in range(len(grid[-1])):
        grid[-1][i] = 1

    sand_origin = (500,0)
    count = 0
    while drop(grid, sand_origin[0]-min_x+buffer, sand_origin[1]):
        # print_grid(grid)
        count += 1

    print_grid(grid)
    return count


def main():
    print("Part One: ")
    print("Test:", part_one(test, "test"))
    print("Result:", part_one(data, "real"))
    print("\nPart Two: ")
    print("Test:", part_two(test, "test"))
    print("Result:", part_two(data, "real"))


if __name__ == "__main__":
    main()

