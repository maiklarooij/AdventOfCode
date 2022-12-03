def get_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38

def part1():

    f = open('day3.txt', 'r')
    total = 0
    for line in f.readlines():

        rucksack = line.strip()
        length = len(rucksack)

        com1 = line[:int(length/2)]
        com2 = line[int(length/2):]

        total += get_priority(set(com1).intersection(set(com2)).pop())

    print(total)

def part2():
    
    f = open('day3.txt', 'r')
    rucksacks = [i.strip() for i in f.readlines()]
    groups = []

    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])

    total = 0
    for group in groups:
        common = set(group[0]).intersection(set(group[1]).intersection(set(group[2])))
        total += get_priority(common.pop())

    print(total)

part1()
part2()
