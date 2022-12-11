from utils import read_input

raw_input = read_input(2)

### Part 1 ###
letter_mapping = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

self_op_earnings_matrix = [
    [1 + 3, 1 + 0, 1 + 6],  # ROCK
    [2 + 6, 2 + 3, 2 + 0],  # PAPER
    [3 + 0, 3 + 6, 3 + 3],  # SCISSOR
]

score = 0
for game in raw_input.split("\n"):
    choices = game.split(" ")
    op = letter_mapping[choices[0]]
    me = letter_mapping[choices[1]]
    score += self_op_earnings_matrix[me][op]
print(score)

### Part 2 ###
op_outcome_self_matrix = [
    [2, 0, 1],
    [0, 1, 2],
    [1, 2, 0]
]
score = 0
for game in raw_input.split("\n"):
    choices = game.split(" ")
    op = letter_mapping[choices[0]]
    outcome = letter_mapping[choices[1]]
    me = op_outcome_self_matrix[op][outcome] 
    score += self_op_earnings_matrix[me][op]
print(score)