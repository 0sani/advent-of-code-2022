with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def part_one(data):
    data = [[int(char) for char in list(line)] for line in data]
    
    visible = set()

    rows, cols = len(data), len(data[0])

    for i, row in enumerate(data):
        # left -> right
        highest = row[0]-1
        for j, val in enumerate(row):
            if val > highest:
                visible.add((i,j))
                highest = val
        
        # right -> left
        highest = row[-1]-1
        for j, val in reversed(list(enumerate(row))):
            if val > highest:
                visible.add((i,j))
                highest = val
        
    for j in range(cols):

        # top -> bottom
        highest = data[0][j]-1
        for i in range(rows):
            if data[i][j] > highest:
                visible.add((i,j))
                highest = data[i][j]
        
        # bottom -> top
        highest = data[-1][j]-1
        for i in range(rows-1,-1,-1):
            if data[i][j] > highest:
                visible.add((i,j))
                highest = data[i][j]

    return len(visible)

def part_two(data):
    data = [[int(char) for char in list(line)] for line in data]

    rows, cols = len(data), len(data[0])

    big = 0

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if i != 0 and i != rows-1 and j != 0 and j != cols-1:   
                product = 1
                # left
                y = 1
                while j-y > 0 and data[i][j-y] < val:
                    y += 1
                product *= y
                # right
                y = 1
                while j+y < cols-1 and data[i][j+y] < val:
                    y += 1
                product *= y
                # up
                x = 1
                while i-x > 0 and data[i-x][j] < val:
                    x += 1
                product *= x
                # down
                x = 1
                while i+x < rows-1 and data[i+x][j] < val:
                    x += 1
                product *= x

                big = max(big, product)
    
    return big


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

