from collections import defaultdict

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def neighbors_gen(rows, cols):
    def helper(i, j):
        n = []
        if i > 0:
            n.append((i-1, j))
        if i < rows -1:
            n.append((i+1, j))
        if j > 0:
            n.append((i, j-1))
        if j < cols -1:
            n.append((i, j+1))
        return n
    return helper

class Graph(): 
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, src, dest):
        self.graph[src].append(dest)
    
    def BFS(self, src, dest):
        explored = [False for _ in range(len(self.graph))]

        Q = [[src]]

        while Q:
            path = Q.pop(0)
            v = path[-1]

            if not explored[v]:
                for edge in self.graph[v]:
                    new = list(path)
                    new.append(edge)
                    Q.append(new)
                
                    if edge in dest:
                        return new
                explored[v] = True

    def __str__(self) -> str:
        return str(self.graph)



def part_one(data):
    data = [list(line) for line in data]

    graph = Graph()

    rows = len(data)
    cols = len(data[0])

    neighbors = neighbors_gen(rows, cols)

    src, dest = -1, -1

    for i in range(rows):
        for j in range(cols):
            square = data[i][j]
            for neighbor in neighbors(i,j):
                if square == "S":
                    src = i *cols + j
                    square = '`'
                elif square == "E":
                    square = '{'
                    dest = i*cols + j

                curr = data[neighbor[0]][neighbor[1]]
                if curr == "S":
                    curr = '`'
                elif curr == "E":
                    curr = '{'
                
                if ord(curr) - ord(square) <= 1:
                    graph.add_edge(i*cols + j, neighbor[0]*cols + neighbor[1])

    parents = graph.BFS(src,[dest])
    return len(parents) -1


def part_two(data):
    data = [list(line.replace("S","a")) for line in data]

    graph = Graph()

    rows = len(data)
    cols = len(data[0])

    neighbors = neighbors_gen(rows, cols)

    dests = []

    for i in range(rows):
        for j in range(cols):
            square = data[i][j]
            for neighbor in neighbors(i,j):
                if square == "a":
                    dests.append(i*cols + j)

                if square == "E":
                    square = '{'
                    src = i*cols + j

                curr = data[neighbor[0]][neighbor[1]]
                if curr == "E":
                    curr = '{'
                
                if ord(curr) - ord(square) >= -1:
                    graph.add_edge(i*cols + j, neighbor[0]*cols + neighbor[1])

    path = graph.BFS(src, dests)
    return len(path)-1

def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Test:", part_two(test))
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

