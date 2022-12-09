# from utils.structures import *

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

with open("test2.txt", "r") as f:
    test2 = [line.strip() for line in f.readlines() if line[0] != "#"]
    f.close()

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def move(self, pair):
        self.x += pair[0]
        self.y += pair[1]

    def x_dist(self, other):
        return abs(self.x - other.x)
    
    def y_dist(self, other):
        return abs(self.y - other.y)

directions = {
    "L": (-1,0),
    "R": (1,0),
    "U": (0,1),
    "D": (0,-1),
}

def display(knots, xmin, xmax, ymin, ymax):
    for i in range(ymax,ymin-1,-1):
        for j in range(xmin, xmax):
            out = ""
            if i == 0 and j == 0:
                out = "s"
            for k, knot in enumerate(knots):
                if knot.x == j and knot.y == i:
                    out = k
            if out == "":
                out = "."
            print(out, end="")
        print("")

def part_one(data):
    data = [line.split() for line in data]

    visited = set()
    H = Point(0,0)
    T = Point(0,0)
    for line in data:
        dir, mag = line[0], int(line[1])

        for i in range(mag):
            H.move(directions[dir])
            if (dir == "L" or dir == "R") and H.x_dist(T)==2:
                T.move(directions[dir])
                T.y = H.y
            elif H.y_dist(T) == 2:
                T.move(directions[dir])
                T.x = H.x
            visited.add((T.x, T.y))

    return len(visited)


def part_two(data):
    data = [line.split() for line in data]

    visited = set()

    knots = [Point(0,0) for _ in range(10)]


    for line in data:
        dir, mag = line[0], int(line[1])
        for _ in range(mag):
            knots[0].move(directions[dir])
            for i in range(1,10):
                H = knots[i-1]
                T = knots[i]
                if T.x_dist(H) == 2 and T.y_dist(H) == 2:
                    T.move(((H.x-T.x)//2, (H.y-T.y)//2))
                elif T.x_dist(H)==2:
                    T.move(((H.x-T.x)//2, 0))
                    T.y = H.y
                elif H.y_dist(T) == 2:
                    T.move((0,(H.y-T.y)//2))
                    T.x = H.x
            T = knots[-1]
            visited.add((T.x, T.y))
        # display(knots, -11, 15, -5, 15)


    return len(visited)


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Test 2:", part_two(test2))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

