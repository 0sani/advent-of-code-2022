with open("input.txt", "r") as f:
    data = f.read().strip()
    f.close()

with open("test.txt", "r") as f:
    test = f.read().strip()
    f.close()

def part_one(data):
    for i in range(4, len(data)):
        if len(list(set(data[i-4:i]))) == 4:
            return i
    
def part_two(data):
    for i in range(14, len(data)):
        if len(list(set(data[i-14:i]))) == 14:
            return i

def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

