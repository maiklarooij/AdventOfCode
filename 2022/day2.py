f = open('day2.txt', 'r')

def calculate_score(opponent, you):
    
    scores = {"X": 1, "Y": 2, "Z": 3}
    wins = {"A": "Y", "B": "Z", "C": "X"}

    if opponent == you:
        return scores[you] + 3
    if wins[opponent] == you:
        return scores[you] + 6
    else:
        return scores[you] + 0


total = 0
for line in f.readlines():

    opponent, you = tuple(line.split())

    total += calculate_score(opponent, you)

print(total)