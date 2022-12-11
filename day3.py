from utils import read_input

raw_input = read_input(3)

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_mapping = {letter: (i+1) for i, letter in enumerate(alphabet)}

### Part 1 ###
score = 0
for pack in raw_input.split("\n"):
    mid = len(pack) // 2
    pack1 = { item for item in pack[:mid] }
    pack2 = { item for item in pack[mid:] }
    dup_item = pack1.intersection(pack[mid:]).pop()
    score += letter_mapping[dup_item]
print(score)

score = 0
packs = raw_input.split("\n")
for i in range(int(len(packs) / 3)):
    pack1, pack2, pack3 = packs[i*3], packs[i*3+1], packs[i*3+2]
    dup_item = set(pack1).intersection(set(pack2)).intersection(set(pack3)).pop()
    score += letter_mapping[dup_item]
print(score)