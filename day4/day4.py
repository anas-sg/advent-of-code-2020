'''part 1
count = 0
expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
received_fields = set()

with open("input.txt") as f:
    for line in f:
        if line != '\n':
            fields = {i[:3] for i in line.split(' ')}
            received_fields.update(fields)
        else:
            print(received_fields, end=' ')
            difference = expected_fields - received_fields
            print("Missing:", difference, end=' ')
            if not difference:
                count += 1
                print("valid")
            else:
                print()
            received_fields.clear()
            
print(count)'''

#part 2
count = 0
expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
received_fields = set()
received_pairs = {}
with open("input.txt") as f:
    for line in f:
        if line != '\n':
            for pair in line.split(' '):
                key, value = pair.split(':')
                received_pairs[key.strip()] = value.strip()
                received_fields.add(key)
        else:
            difference = expected_fields - received_fields
            if not difference:
                rules = {
                    'byr': lambda x: 1920 <= int(x) <= 2002,
                    'iyr': lambda x: 2010 <= int(x) <= 2020,
                    'eyr': lambda x: 2020 <= int(x) <= 2030,
                    'hgt': lambda x: 150 <= int(x[:-2]) <= 193 if x[-2:] == 'cm' \
                                else 59 <= int(x[:-2]) <= 76 if x[-2:] == 'in' else False,
                    'hcl': lambda x: x[0] == '#' and len(x) == 7 and \
                                all(map(lambda y: '0' <= y <= '9' or 'a' <= y <= 'f', x[1:])),
                    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
                    'pid': lambda x: len(x) == 9 and all(map(lambda y: '0' <= y <= '9', x)),
                    'cid': lambda x: True
                }
                for key in received_pairs:
                    if not rules[key](received_pairs[key]):
                        break
                else:
                    count += 1
            received_fields.clear()
            received_pairs.clear()            
print(count)