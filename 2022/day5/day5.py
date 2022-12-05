f = open('day5.txt', 'r')

lines = f.readlines()
crates = {i: [] for i in range(1, 10)}

for line in reversed(lines[:8]):

    for crate, i in enumerate(range(1, 36, 4), start=1):
        
        if line[i] != ' ':
            crates[crate].append(line[i])

for instruction in lines[10:]:
    
    parts = instruction.strip().split()
    times = int(parts[1])
    source = int(parts[3])
    dest = int(parts[5])

    items = reversed([crates[source].pop() for i in range(times)])
    
    for item in items:
        crates[dest].append(item)

print(crates)