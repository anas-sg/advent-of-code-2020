puzzle_input = []
with open("input.txt") as f:
    for line in f:
        puzzle_input.append(int(line))

length = len(puzzle_input)
# for i in range(length - 1):
#     for j in range(i + 1, length):
#         if puzzle_input[i] + puzzle_input[j] == 2020:
#             # print("Found", i, j)
#             break
#     else:
#         continue
#     break
# print(puzzle_input[i] * puzzle_input[j])

for i in range(length - 1):
    for j in range(i + 1, length):
        for k in range(j + 1, length - 2):
            if puzzle_input[i] + puzzle_input[j] + puzzle_input[k] == 2020:
                # print("Found", i, j, k)
                # print(puzzle_input[i] * puzzle_input[j] * puzzle_input[k])
                break
        else:
            continue
        break
    else:
        continue
    break

# print(i, j, k)
print(f"The numbers are {puzzle_input[i]}, {puzzle_input[j]} and {puzzle_input[k]}")
print(f"{puzzle_input[i]} * {puzzle_input[j]} * {puzzle_input[k]} = {puzzle_input[k] * puzzle_input[j] * puzzle_input[i]}")
# for i in range(length - 1):
#     print(puzzle_input[i] * 2)
