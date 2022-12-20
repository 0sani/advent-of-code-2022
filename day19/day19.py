import re

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    f.close()

with open("test.txt", "r") as f:
    test = [line.strip() for line in f.readlines()]
    f.close()


def blueprint_sim(cost_mat,time=24):
    curr_best = [0]

    memoization = {}
    def helper(time, ore, clay, obsidian, geode, or_r, cl_r, ob_r, ge_r):
        cond = (time, ore, clay, obsidian, geode, or_r, cl_r, ob_r, ge_r)
        if (cond in memoization):
            return memoization[cond]


        if time == 0:
            return geode

        if curr_best[0] > geode + (time*(time+1) / 2) + time*ge_r:
            return 0

        options = []

        # build geode robot
        geo_plan = cost_mat[3]
        if ore >= geo_plan[0] and clay >= geo_plan[1] and obsidian >= geo_plan[2]:
            geo_build = helper(time-1, 
                ore-geo_plan[0]+or_r, clay-geo_plan[1]+cl_r, obsidian-geo_plan[2]+ob_r, geode + ge_r,
                or_r, cl_r, ob_r, ge_r+1)
            options.append(geo_build)
        
        # build obsidian robot
        ob_plan = cost_mat[2]
        if ore >= ob_plan[0] and clay >= ob_plan[1] and obsidian >= ob_plan[2]:
            if or_r < max([cost_mat[i][2] for i in range(len(cost_mat))]):
                ob_build = helper(time-1, 
                ore-ob_plan[0]+or_r, clay-ob_plan[1]+cl_r, obsidian-ob_plan[2]+ob_r, geode + ge_r,
                or_r, cl_r, ob_r+1, ge_r)
                options.append(ob_build)

        # build clay robot
        cl_plan = cost_mat[1]
        if ore >= cl_plan[0] and clay >= cl_plan[1] and obsidian >= cl_plan[2]:
            if or_r < max([cost_mat[i][1] for i in range(len(cost_mat))]):
                cl_build = helper(time-1, 
                ore-cl_plan[0]+or_r, clay-cl_plan[1]+cl_r, obsidian-cl_plan[2]+ob_r, geode + ge_r,
                or_r, cl_r+1, ob_r, ge_r)
                options.append(cl_build)

        # build ore robot
        ore_plan = cost_mat[0]
        if ore >= ore_plan[0] and clay >= ore_plan[1] and obsidian >= ore_plan[2]:
            if or_r < max([cost_mat[i][0] for i in range(len(cost_mat))]):
                ore_build = helper(time-1, 
                ore-ore_plan[0]+or_r, clay-ore_plan[1]+cl_r, obsidian-ore_plan[2]+ob_r, geode + ge_r,
                or_r+1, cl_r, ob_r, ge_r)
                options.append(ore_build)
        


        # do nothing
        nothing = helper(time-1, ore + or_r, clay + cl_r, obsidian+ob_r, geode + ge_r, or_r, cl_r, ob_r, ge_r)
        options.append(nothing)
        
        best = max(options)
        memoization[cond] = best
        curr_best[0] = max(curr_best[0], best)
        return best

    out = helper(time, 0,0,0,0, 1,0,0,0)
    return out


def part_one(data):
    costs = []
    for line in data:
        cost_mat = [[0 for i in range(3)] for j in range(4)]
        recipies = re.findall("(\d .*?)\.",line)
        for i, part in enumerate(recipies):
            if "and" in part:
                part = part.split(" and ")
            else:
                part = [part]
            for subpart in part:
                if "ore" in subpart:
                    cost_mat[i][0] = int(subpart.split(" ")[0])
                elif "clay" in subpart:
                    cost_mat[i][1] = int(subpart.split(" ")[0])
                else:
                    cost_mat[i][2] = int(subpart.split(" ")[0])
        costs.append(cost_mat)

    total = 0
    for i in range(len(data)):
        geodes = blueprint_sim(costs[i], 24)
        print(f"Blueprint #{i+1}: {geodes}")
        total += (i+1) * geodes 

    
    return total

def part_two(data):
    costs = []
    for line in data:
        cost_mat = [[0 for i in range(3)] for j in range(4)]
        recipies = re.findall("(\d .*?)\.",line)
        for i, part in enumerate(recipies):
            if "and" in part:
                part = part.split(" and ")
            else:
                part = [part]
            for subpart in part:
                if "ore" in subpart:
                    cost_mat[i][0] = int(subpart.split(" ")[0])
                elif "clay" in subpart:
                    cost_mat[i][1] = int(subpart.split(" ")[0])
                else:
                    cost_mat[i][2] = int(subpart.split(" ")[0])
        costs.append(cost_mat)

    total = 1
    for i in range(3):
        geodes = blueprint_sim(costs[i], 32)
        print(geodes)
        total *= geodes

    
    return total


def main():
    print("Part One: ")
    print("Test:", part_one(test))
    print("Result:", part_one(data))
    print("\nPart Two: ")
    print("Result:", part_two(data))


if __name__ == "__main__":
    main()

