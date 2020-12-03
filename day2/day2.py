count = 0
# with open("input.txt") as f:
#     for line in f:
#         rule, letter, password = line.split()
#         rule = [int(i) for i in rule.split('-')]
#         letter = letter[0]
#         if rule[0] <= password.count(letter) <= rule[1]:
#             count += 1
# print(count)

with open("input.txt") as f:
    for line in f:
        rule, letter, password = line.split()
        rule = [int(i) for i in rule.split('-')]
        letter = letter[0]
        if password[rule[0]-1] == letter:
            if password[rule[1]-1] != letter:
                count += 1
        elif password[rule[1]-1] == letter:
            count += 1
        
print(count)
