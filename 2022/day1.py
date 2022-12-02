f = open('day1.txt', 'r')

elf = 0
elfs = []
for line in f.readlines():

    if line.strip():
        elf += int(line.strip())
    else:
        elfs.append(elf)
        elf = 0

print(sum(sorted(elfs, reverse=True)[:3]))