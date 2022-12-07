f = open('day6.txt', 'r')

stream = f.read()

for i in range(len(stream)):

    if len(set(stream[i-13:i+1])) == 14:
        print(i+1)
        break

