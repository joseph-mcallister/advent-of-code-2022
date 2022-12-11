from utils import read_input

raw_input = read_input(1)

### Part 1 ###
max_calories = max(
    [
        sum(int(calorie) for calorie in calories.split("\n"))
        for calories in raw_input.split("\n\n")
    ]
)
print(max_calories)  # 65912

### Part 2 ###
top_3_calories = sum(
    sorted(
        [
            sum(int(calorie) for calorie in calories.split("\n"))
            for calories in raw_input.split("\n\n")
        ]
    )[-3:]
)
print(top_3_calories)
