with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()

def parse(data):
    out = []
    
    for line in data:
        line = line.split()
        out.append((
            int(line[2].split("=")[1][:-1]),
            int(line[3].split("=")[1][:-1]),
            int(line[-2].split("=")[1][:-1]),
            int(line[-1].split("=")[1])
        ))
    return out

def manhattan_dist(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)


def part_one(data, slice):
    data = parse(data)


    beacons = []
    dists = {}

    for datum in data:
        sx, sy, bx, by = datum

        dist = manhattan_dist(sx,sy,bx,by)
        beacons.append((bx, by))
        dists[(sx, sy)] = dist
    

    min_x = float(1e12)
    max_x = float(-1e12)
    for dist in dists.items():
        min_x = min(min_x, dist[0][0]-dist[1])
        max_x = max(max_x, dist[0][0]+dist[1])


    print(min_x, max_x)

    covered = 0
    for i in range(min_x-1, max_x+1):
        # x = covered
        for entry in dists.items():
            point = entry[0]
            dist = entry[1]

            if manhattan_dist(point[0], point[1], i, slice) <= dist and (i, slice) not in beacons:
                covered += 1
                break
        # if ((i, slice) in beacons):
        #     print("B", end="")
        # elif x != covered:
        #     print("#",end="")
        # else:
        #     print(".",end="")


    return covered

def part_two(data, bound):
    data = parse(data)


    beacons = []
    dists = {}

    for datum in data:
        sx, sy, bx, by = datum

        dist = manhattan_dist(sx,sy,bx,by)
        beacons.append((bx, by))
        dists[(sx, sy)] = dist
    
    def is_covered(x,y):
        for entry in dists.items():
                point = entry[0]
                dist = entry[1]
                # if manhattan_dist(point[0], point[1], x, y) <= dist and (x, y) not in beacons:
                if manhattan_dist(point[0], point[1], x, y) <= dist:
                    return True
        return False



    # for i in range(bound):
    #     for j in range(bound):
    #         if (i,j) in beacons:
    #             print("B ",end="")
    #         elif (i, j) in dists:
    #             print("S ",end="")
    #         elif is_covered(i, j):
    #             print("# ",end="")
    #         else:
    #             print(". ", end="")
    #     print("")

    for entry in dists.items():
        point = entry[0]
        dist = entry[1]

        print("Entry: ", point, dist)
        for i in range(dist+2):
            l, r, t, d = point[0] - i, point[0]+i, point[1]+dist + 1 - i, point[1]-dist - 1 + i
            # print(l,r,t, d)
            if 0 <= l <= bound and 0 <= t <= bound and (not is_covered(l,t)):
                return l * 4000000 + t
            if 0 <= r <= bound and 0 <= t <= bound and (not is_covered(r,t)):
                return r * 4000000 + t
            if 0 <= l <= bound and 0 <= d <= bound and (not is_covered(l,d)):
                return l * 4000000 + d
            if 0 <= r <= bound and 0 <= d <= bound and (not is_covered(r,d)):
                return r * 4000000 + d

    return False



def main():
    print("Part One: ")
    # print("Test:", part_one(test, 10))
    # print("Result:", part_one(data, 2000000))
    print("\nPart Two: ")
    print("Test:", part_two(test,21))
    print("Result:", part_two(data,4000000))


if __name__ == "__main__":
    main()

