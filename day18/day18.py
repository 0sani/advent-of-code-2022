with open("input.txt", "r") as f:
    data = [[int(num) for num in line.strip().split(",")] for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [[int(num) for num in line.strip().split(",")] for line in f.readlines()]
    f.close()

def get_neighbors(grid, x,y,z):
    neighbors = []
    x_max, y_max, z_max = len(grid),len(grid[0]),len(grid[0][0])
    if (x-1) > 0:
        neighbors.append((x-1,y,z))
    if (x+1) < x_max:
        neighbors.append((x+1,y,z))
    if (y-1) > 0:
        neighbors.append((x,y-1,z))
    if (y+1) < y_max:
        neighbors.append((x,y+1,z))
    if (z-1) > 0:
        neighbors.append((x,y,z-1))
    if (z+1) < z_max:
        neighbors.append((x,y,z+1))
    return neighbors

def part_one(data):
    total = len(data)*6
    for i, p1 in enumerate(data):
        for j, p2 in enumerate(data[i+1:]):
            if p1[0] == p2[0] and p1[1] == p2[1] and abs(p1[2]-p2[2]) == 1:
                total -= 2
            elif p1[0] == p2[0] and abs(p1[1]-p2[1])==1 and p1[2] == p2[2]:
                total -= 2
            elif abs(p1[0]-p2[0])==1 and p1[1] == p2[1] and p1[2] == p2[2]:
                total -= 2


    return total
    
def part_two(data):
    x_max = max(data, key=lambda item: item[0])[0]
    y_max = max(data, key=lambda item: item[1])[1]
    z_max = max(data, key=lambda item: item[2])[2]
    b = buffer = 4
    grid = [[[0 for i in range(z_max+b)] for j in range(y_max+b)] for k in range(x_max+b)]

    for p in data:
        x,y,z = p
        grid[x][y][z] = 1


    visited = [[[0 for i in range(z_max+b)] for j in range(y_max+b)] for k in range(x_max+b)]

    size_x = len(grid)
    size_y = len(grid[0])
    size_z = len(grid[0][0])

    def DFS(grid, x,y,z):
        faces = 0
        stack = []
        stack.append((x,y,z))
        while stack:
            x,y,z = stack.pop()
            if visited[x][y][z] == 0:
                visited[x][y][z] = 1
                for i,j,k in get_neighbors(grid,x,y,z):
                    if grid[i][j][k] == 0:
                        stack.append((i,j,k))
                    else: 
                        faces += 1
        return faces
    
    outside = DFS(grid,0,0,0)
    inside = []
    for i in range(size_x):
        for j in range(size_y):
            for k in range(size_z):
                if visited[i][j][k] == 0 and grid[i][j][k] == 0:
                    inside.append(DFS(grid, i,j,k))
    return part_one(data) - sum(inside)


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

