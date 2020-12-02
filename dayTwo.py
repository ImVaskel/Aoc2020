from utility import get_data_string

data = get_data_string("day-two-data.txt")
new_data = []

for i in data:
    j = i.split()
    j[1] = j[1][0]
    x = j[0].split("-")
    j[0] = tuple(x)
    new_data.append(j)

class Solution:
    def __init__(self, min, max, char, string):
        self.min = int(min)
        self.max = int(max)
        self.char = char
        self.string = string

    def is_valid(self) -> bool:
        occurrences = 0
        for i in range(len(self.string)):
            if self.string[i] == self.char:
                occurrences += 1
            if occurrences > self.max:
                return False
            if i == len(self.string)-1:
                if occurrences >= self.min:
                    return True

    def is_valid_part2(self):
        if self.string[self.min-1] == self.char and self.string[self.max-1] == self.char:
            return False
        elif self.string[self.min-1] == self.char or self.string[self.max-1] == self.char:
            return True
        else:
            return False


classed_data = [Solution(i[0][0], i[0][1], i[1], i[2]) for i in new_data]

valid = [i.is_valid() for i in classed_data if i.is_valid()]
valid_part2 = [i.is_valid_part2() for i in classed_data if i.is_valid_part2()]
print(f"{len(valid)} \n{len(valid_part2)}")
