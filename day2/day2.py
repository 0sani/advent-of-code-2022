with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

options = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

result = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

def part_one(data):
    data = [d.split() for d in data]
    total = 0
    for hand in data:
        them, you = hand[0], hand[1]
        if them == "A":
            if you == "X":
                total += 4
            elif you == "Y":
                total += 8
            else:
                total += 3
        elif them == "B":
            if you == "X":
                total += 1
            elif you == "Y":
                total += 5
            else:
                total += 9
        elif them == "C":
            if you == "X":
                total += 7
            elif you == "Y":
                total += 2
            else:
                total += 6
    return total

def part_two(data):
    data = [d.split() for d in data]
    total = 0
    for hand in data:
        them, you = hand[0], hand[1]
        total += result[you]
        if you == "X":
            x = options[them] - 1
            if x == 0:
                x = 3
            total += x
        elif you == "Y":
            total += options[them]
        else: 
            x = options[them] + 1
            if x == 4:
                x = 1
            total += x
            # 1 -> 2, 2 -> 3, 3 -> 1
    
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