with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

# with open("test.txt", "r") as f:
#     data = [line.strip() for line in f.readlines()]
#     f.close()

def part_one():
    highest = 0
    curr = 0
    for line in data:
        if line == "":
            highest = max(highest, curr)
            curr = 0
        else:
            curr += int(line)
    return highest

def part_two():
    elves = []
    curr = 0
    for line in data:
        if line == "":
            elves.append(curr)
            curr = 0
        else:
            curr += int(line)
    
    elves.sort(reverse=True)

    return sum(elves[:3])


def main():
    print("Part One: ", part_one())
    print("Part Two: ", part_two())


if __name__ == "__main__":
    main()