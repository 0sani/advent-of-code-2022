with open("input.txt", "r") as f:
	a = [line for line in f.readlines()]
	f.close()

with open("test.txt", "r") as f:
	b = [line for line in f.readlines()]
	f.close()


def p1(data):
	# get line at bottom of stack
	ind = 0
	while data[ind].strip().split()[0] != "1":
		ind += 1
	stacks = [[] for i in range(int(data[ind].split()[-1]))]
	
	for i in range(ind-1, -1, -1):
		line = data[i]
		for i in range(len(stacks)):
			num = line[4*i:4*i+3]
			if "A" <= num[1] <= "Z":
				stacks[i].append(num[1])
	
	for line in data[ind+2:]:
		parts = line.split(" ")
		quant, start, dest = int(parts[1]), int(parts[3])-1, int(parts[5].strip())-1
		for i in range(quant):
			stacks[dest].append(stacks[start].pop(-1))
	
	out = ""
	for stack in stacks:
		out += stack.pop(-1)
	return out


def p2(data):
	# get line at bottom of stack
	ind = 0
	while data[ind].strip().split()[0] != "1":
		ind += 1
	stacks = [[] for i in range(int(data[ind].split()[-1]))]
	
	for i in range(ind-1, -1, -1):
		line = data[i]
		for i in range(len(stacks)):
			num = line[4*i:4*i+3]
			if "A" <= num[1] <= "Z":
				stacks[i].append(num[1])
	
	for line in data[ind+2:]:
		parts = line.split(" ")
		quant, start, dest = int(parts[1]), int(parts[3])-1, int(parts[5].strip())-1
		stacks[dest].extend(stacks[start][-quant:])
		for i in range(quant):
			stacks[start].pop(-1)
	
	out = ""
	for stack in stacks:
		out += stack.pop(-1)
	return out

print(p1(b))
print(p1(a))
print(p2(b))
print(p2(a))
