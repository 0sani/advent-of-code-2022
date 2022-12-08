import re

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

class Dir:
    def __init__(self, name=None, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self.contents = {}
    
    def size(self):
        return sum(self.contents.values()) + sum([child.size() for child in self.children.values()])

    def __str__(self):
        return self.name +" "+ str(self.size()) + "\n" + "\n".join([str(i) for i in self.contents.items()]) + "\n"+ "\n".join([str(i) for i in self.children.values()])


def parse(data):
    base = Dir()
    base.children["/"] = Dir("/", base)
    cwd = base
    for line in data:
        # cd 
        match = re.search("^\$ cd (.*)", line)
        if match:
            name = match.group(1)
            if name == "..":
                cwd = cwd.parent
            else:
                cwd = cwd.children[name]

        else:
            if (not re.search("^\$ ls", line)):
                dir = re.search("^dir (.*)",line)
                if (dir):
                    cwd.children[dir.group(1)] = Dir(dir.group(1), cwd)
                else:
                    file = re.search("^(\d+) (.*)", line)
                    cwd.contents[file.group(2)] = int(file.group(1))
    return base.children["/"]


def part_one(data):
    dir = parse(data)
    def helper(cwd, max_size=100000):
        total = 0
        if cwd.size() <= max_size:
            total += cwd.size()
        return total + sum([helper(child, max_size) for child in cwd.children.values()])
    return helper(dir)


def part_two(data):
    dir = parse(data)
    smallest = [float("inf")]
    def helper(dir, min_size, ):
        if dir.size() >= min_size:
            smallest[0] = min(dir.size(), smallest[0])
        [helper(child, min_size) for child in dir.children.values()]
    
    min_size = dir.size() - 40000000
    helper(dir,min_size)
    return smallest[0]


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()



# 