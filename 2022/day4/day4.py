f = open('day4.txt', 'r')

count = 0
for line in f.readlines():

    elf1, elf2 = tuple(line.strip().split(','))
    
    elf1_start, elf1_end = tuple([int(num) for num in elf1.split('-')])
    elf2_start, elf2_end = tuple([int(num) for num in elf2.split('-')])

    elf1_set = {i for i in range(elf1_start, elf1_end + 1)}
    elf2_set = {i for i in range(elf2_start, elf2_end + 1)}

    if elf1_set.intersection(elf2_set):
        count += 1

print(count)