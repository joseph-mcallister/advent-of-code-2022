from utils import read_input

raw_input = read_input(4)

### Part 1 ###
pairs_raw = raw_input.split("\n")
pairs = []
for pair in pairs_raw:
    left, right = pair.split(",")
    left_start, left_end = left.split("-")
    right_start, right_end = right.split("-")
    pairs.append((int(left_start), int(left_end), int(right_start), int(right_end)))

count_fully_overlapped = 0
for pair in pairs:
    left_start, left_end, right_start, right_end = pair
    if left_start <= right_start and left_end >= right_end:
        count_fully_overlapped += 1
    elif right_start <= left_start and right_end >= left_end:
        count_fully_overlapped += 1
print(count_fully_overlapped)

### Part 2 ###
count_partially_overlapped = 0
for pair in pairs:
    left_start, left_end, right_start, right_end = pair
    if left_start <= right_start and left_end >= right_start:
        count_partially_overlapped += 1
    elif right_start <= left_start and right_end >= left_start:
        count_partially_overlapped += 1
print(count_partially_overlapped)