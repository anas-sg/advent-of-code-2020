with open("input.txt") as f:
    puzzle = [list(line[:-1]) for line in f]

# row = column = 0
# rows = len(puzzle)
# columns = len(puzzle[0])
# count = 0
# while row < rows:
#     row, column = row + 1, column + 3
#     try:
#         if puzzle[row][column % columns] == '#':
#             count += 1
#     except:
#         break
# print(count)

rows = len(puzzle)
columns = len(puzzle[0])
product = 1
for i, j in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    row = column = count = 0
    while row < rows:
        row, column = row + j, column + i
        try:
            if puzzle[row][column % columns] == '#':
                count += 1
        except:
            break
    product *= count

print(product)