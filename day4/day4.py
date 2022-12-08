with open("input.py", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.py", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def part_one(data):
    count =0
    for line in data:
        r1,r2 = line.split(",")
        x1, y1 = r1.split("-")
        x2, y2 = r2.split("-")
        if (int(x1) <= int(x2) and int(y1) >= int(y2)):

            count += 1
        elif (int(x1) >= int(x2) and int(y1) <= int(y2)):

            count += 1
            
    return count

def part_two(data):
    count =0
    for line in data:
        r1,r2 = line.split(",")
        x1, y1 = [int(i) for i in r1.split("-")]
        x2, y2 = [int(i) for i in r2.split("-")]
        if (max(x1,x2,y1,y2) - min(x1,x2,y1,y2)) <= (abs(x1-y1)+abs(x2-y2)):
            count += 1
            #print(x1,x2,y1,y2)
            #print(max(x1,x2,y1,y2) - max(x1,x2,y1,y2))
            #print(abs(x1-y1)+abs(x2-y2))
    return count

def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

