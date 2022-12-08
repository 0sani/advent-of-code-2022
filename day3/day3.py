with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def part_one(data):
    pairs = [[line[:len(line)//2], line[len(line)//2:]] for line in data]
    total = 0
    for pair in pairs:
        x, y  = set(pair[0]), set(pair[1])
        z = ord(list(x.intersection(y))[0])

        if 64 < z < 91:
            total += 26 + z - 64
        elif 96 < z < 123:
            total += z - 96
    return total

def part_two(data):
    total = 0
    for i in range(0, len(data), 3):
        x, y, z = set(data[i]), set(data[i+1]), set(data[i+2])
        z = ord(list(x.intersection(y, z))[0])

        if 64 < z < 91:
            total += 26 + z - 64
        elif 96 < z < 123:
            total += z - 96
    return total
    


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()
