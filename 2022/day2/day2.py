f = open('day2.txt', 'r')

def calculate_score_part1(opponent, you):
    
    scores = {"X": 1, "Y": 2, "Z": 3}
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}

    if draws[opponent] == you:
        return scores[you] + 3
    if wins[opponent] == you:
        return scores[you] + 6
    else:
        return scores[you] + 0

def calculate_score_part2(opponent, outcome):
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}
    loses = {"A": "Z", "B": "X", "C": "Y"}

    if outcome == 'Y':
        return calculate_score_part1(opponent, draws[opponent])
    elif outcome == 'X':
        return calculate_score_part1(opponent, loses[opponent])
    else:
        return calculate_score_part1(opponent, wins[opponent])


total = 0
for line in f.readlines():

    opponent, you = tuple(line.split())

    total += calculate_score_part2(opponent, you)

print(total)