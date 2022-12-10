with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def part_one(data):
    data = [line.split() for line in data]

    registers = 1
    cycle = 0
    strength = 0
    for line in data:
        if (len(line) != 1):
            cycle += 1
            if not (cycle + 20) % 40:
                print(registers * cycle, registers, cycle)
                strength += registers * cycle
            cycle += 1
            if not (cycle + 20) % 40:
                print(registers * cycle, registers, cycle)
                strength += registers * cycle
            registers += int(line[1])
        else:
            cycle += 1
            if not (cycle + 20) % 40:
                print(registers * cycle, registers, cycle)
                strength += registers * cycle
    
    return strength



def part_two(data):
    data = [line.split() for line in data]

    reg = 1
    instruction = data.pop(0)
    next_op = len(instruction)
    for i in range(240):
        if i == next_op:
            if len(instruction) == 2:
                reg += int(instruction[1])
            instruction = data.pop(0)
            if len(instruction) == 1:
                next_op += 1
            else:
                next_op += 2
        
        sprite = [reg-1,reg, reg+1]
        if (i%40 in sprite):
            print("#",end="")
        else:
            print(".",end="")
        if (i+1) % 40==0:
            print("")



def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:")
    part_two(test)
    print("Result:")
    part_two(data)


if __name__ == "__main__":
    main()

