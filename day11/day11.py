with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

class Monkey():
    def __init__(self, id, items, op, test, pos, neg) -> None:
        self.id = id
        self.items = items
        self.op = op
        self.test = test
        self.pos = pos
        self.neg = neg
        self.inspections = 0
    

class Group:
    def __init__(self, monkeys) -> None:
        self.monkeys = {monkey.id : monkey for monkey in monkeys}
        self.modulos = 1
        for monkey in monkeys:
            self.modulos *= monkey.test
    
    def turn(self, id, decay):
        monkey = self.monkeys[id]

        while len(monkey.items) != 0:
            item = monkey.items.pop(0)
            monkey.inspections += 1
            # adjust worry level)
            item = monkey.op(item)
            # decay
            if decay:
                item //= 3
            if (item % monkey.test) == 0:
                if not decay:
                    item %= self.modulos
                self.monkeys[monkey.pos].items.append(item)
            else:
                if not decay:
                    item %= self.modulos
                self.monkeys[monkey.neg].items.append(item)


    def total_inspections(self):
        return [monkey.inspections for monkey in self.monkeys.values()]

    def round(self, decay):
        for i in range(len(self.monkeys)):
            self.turn(i, decay)
    
    def __str__(self) -> str:
        return "\n".join([str(monkey.id)+ " " + str(monkey.inspections) for monkey in self.monkeys.values()])

# loop:
# for each item:
#   operation -> bored (decay) -> test -> throw

def op_maker(eval_string):
    def helper(old):
        return eval(eval_string)
    return helper

def test_maker(n):
    def helper(val):
        return val % n == 0
    return helper

def parse(data):
    monkeys = []
    for i in range((len(data)+1)//7):
        items = [int(num) for num in data[i*7+1].split(": ")[1].split(", ")]
        pos = int(data[i*7+4].split(" ")[-1])
        neg = int(data[i*7+5].split(" ")[-1])
        eval_string = data[i*7+2].split("= ")[-1]
        test = int(data[i*7+3].split(" ")[-1])

        monkeys.append(Monkey(i,
                            items, 
                            op_maker(eval_string),
                            test,
                            pos, 
                            neg))
    return Group(monkeys)

def part_one(data):
    monkeys = parse(data)

    for i in range(20):
        monkeys.round(True)

    inspections = sorted(monkeys.total_inspections())
    # print(monkeys)
    return inspections[-1]*inspections[-2]

def part_two(data):
    monkeys = parse(data)

    for i in range(10000):
        # if i == 1 or i == 20 or i == 1000 or i == 2000:
        #     print("Round: ", i)
        #     print(monkeys)
        #     print("")

        monkeys.round(False)

    inspections = sorted(monkeys.total_inspections())
    print(monkeys)
    return inspections[-1]*inspections[-2]


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data ))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

