with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def monkey_eval(instruction, monkeys):
        parts = instruction.split(" ")
        if len(parts) == 1:
            return monkeys[instruction]

        operator = parts[1]
        op1, op2 = parts[0], parts[2]
        if type(monkeys[op1]) != int:
            op1 = monkey_eval(monkeys[op1], monkeys)
        else:
            op1 = monkeys[op1]
        if type(monkeys[op2]) != int:
            op2 = monkey_eval(monkeys[op2], monkeys)
        else:
            op2 = monkeys[op2]

        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return op1 // op2

def solve(a, b):
    operators = ["+", "-", "*", "/"]
    while a != "h":
        # find middle
        paren = 0
        for i, char in enumerate(a):
            if char == "(":
                paren += 1
            elif char == ")":
                paren -= 1
            if paren == 1 and char in operators:
                op = char
                left, right = a[1:i], a[i+1:-1]
                break
        if "h" in left:
            if op == "+":
                b -= eval(right)
            elif op == "-":
                b += eval(right)
            elif op == "*":
                b /= eval(right)
            else:
                b *= eval(right)
            a = left.strip()

        else:
            if op == "+":
                b -= eval(left)
            elif op == "-":
                # x - h = b
                # h = x - b
                b = eval(left) - b
            elif op == "*":
                b /= eval(left)
            else:
                # x / h = b
                # h = x / b
                b = eval(left) / b
            a = right.strip()
    return b

def part_one(data):
    data = [line.split(": ") for line in data]

    monkeys = {}
    for line in data:
        if " " in line[1]:
            monkeys[line[0]] = line[1]
        else:
            monkeys[line[0]] = int(line[1])

    return monkey_eval(monkeys["root"], monkeys)

def part_two(data):
    data = [line.split(": ") for line in data]

    monkeys = {}
    for line in data:
        if " " in line[1]:
            monkeys[line[0]] = line[1]
        else:
            monkeys[line[0]] = int(line[1])

    def gen_paren_eq(instruction):
        parts = instruction.split(" ")
        if len(parts) == 1:
            return str(monkeys[instruction])

        operator = parts[1]
        op1, op2 = parts[0], parts[2]
        if type(monkeys[op1]) != int:
            op1 = gen_paren_eq(monkeys[op1])
        else:
            if op1 != "humn":
                op1 = monkeys[op1]
            else:
                op1 = "h"
        if type(monkeys[op2]) != int:
            op2 = gen_paren_eq(monkeys[op2])
        else:
            if op2 != "humn":
                op2 = monkeys[op2]
            else:
                op1 = "h"

        return f"({op1} {operator} {op2})"

    def human_in_path(instruction):
        if type(instruction) == int:
            return False

        parts = instruction.split(" ")
        if parts[0] == "humn" or parts[2] == "humn":
            return True

        return human_in_path(monkeys[parts[0]]) or human_in_path(monkeys[parts[2]])
    
    # a has the human in it
    options = monkeys["root"].split(" ")
    if human_in_path(monkeys[options[0]]):
        a, b = gen_paren_eq(monkeys[options[0]]), gen_paren_eq(monkeys[options[2]])
    else:
        b, a = gen_paren_eq(monkeys[options[0]]), gen_paren_eq(monkeys[options[2]])
    b = int(eval(b))

    return int(solve(a,b))



def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

