def get_data() -> list:
    l = []
    with open("day-four-data.txt", "r") as f:
        l = [i for i in f.readlines()]
    return l

def convert_data():
    data = get_data()
    l = []
    s = ""
    for line in data:
        if line != "\n":
            s += line
        else:
            l.append(s)
            s = ""

    l = [i.replace("\n", ' ') for i in l]
    return l

def convert_to_dict(p):
    l = []

    for i in p:
        d = {}
        for j in i:
            if j == '': continue
            splitString = j.split(":")
            entry1, entry2 = splitString[0], splitString[1]
            d[entry1] = entry2

        l.append(d)

    return l

def part_1(p):
    valid_pass = []
    invalid_pass = []
    for i in p:
        if p.index(i) == len(p) - 1:
            print(i)
        if set(i.keys()) == {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"} or set(i.keys()) == {"byr", "iyr" , "eyr", "hgt", "hcl", "ecl", "pid"}:
            valid_pass.append(i)

        else:
            invalid_pass.append(i)

    print(len(invalid_pass))
    return valid_pass

l = convert_data()
new_data = [i.split(" ") for i in l]
newer_data = convert_to_dict(new_data)
valid = part_1(newer_data)

#print(len(l))
#print(len(new_data))
#print(len(newer_data))
print(len(valid))





