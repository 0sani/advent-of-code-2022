with open("input.txt", "r") as f:
    data = f.read()
    f.close()

with open("test.txt", "r") as f:
    test = f.read()
    f.close()

def compare(left, right):
    for l, r in zip(left, right):
        if (type(l) == int and type(r) == int):
            if l != r:
                if l < r:
                    return True
                else:
                    return False
        elif (type(l) == list and type(r) == list):
            res = compare(l, r)
            if (res != -1):
                return res
        else:
            if type(l) == int:
                return compare([l], r)
            else:
                return compare(l, [r])
    if len(left) < len(right):
        return True
    elif len(left) == len(right):
        return -1
    else:
        return False

def part_one(data):
    data = data.split("\n\n")
    data = [pair.split("\n") for pair in data]

    total = 0

    x = [[1,2,3],4]
    y = [[1,2,3],3]

    print(compare(x,y))

    for i, pair in enumerate(data):
        left = eval(pair[0])
        right = eval(pair[1])

        if compare(left, right):
            total += i + 1

    return total

def part_two(data):
    data = data.strip().split()

    packets = [eval(line) for line in data]

    packets.append([[2]])
    packets.append([[6]])

    for i, packet in enumerate(packets):
        if i == 0:
            pass

        j = i -1

        while j >= 0 and compare(packet,packets[j]):
            packets[j + 1] = packets[j]
            j -= 1
        packets[j + 1] = packet
    
    l, r = -1, -1

    for i, packet in enumerate(packets):
        if packet == [[2]]:
            l = i+1
        elif packet == [[6]]:
            r = i+1
    
    return l*r


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

