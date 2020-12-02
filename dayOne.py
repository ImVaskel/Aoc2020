from utility import get_data

#Day one, find the values in a list of ints that add to 2020 and then multiply them
def part1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j

#Day 1, part 2, same as above, but 3 value add to 2020
def part2(data):
    for i in data:
        for j in data:
            for p in data:
                if i + j + p == 2020:
                    return i * j * p

data = get_data("day-one-data.txt")

print(part1(data))
print(part2(data))