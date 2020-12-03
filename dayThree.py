from utility import get_data_string

data = get_data_string("day-three-data.txt")

def convert_to_dict():
    """Convert to a dict of x,y coordinates, y being the index of the row in the list"""
    return_dict = {}
    for num in range(len(data)):
        for i in range(len(data[num])):
            return_dict.update({(i, num): data[num][i]})
    return return_dict

def get_solution(input):
    x = 0
    y = 0
    l = []
    l.append(input[(x, y)])
    while y <= len(data):
        if x + 3 > 30:
            x += 3
            x = abs(31 - x)
        else: x += 3
        y += 1
        try: l.append(input[(x, y)])
        except: return l
    return l

def get_solution_slope(input, slope_x, slope_y):
    x = 0
    y = 0
    l = []
    l.append(input[(x, y)])
    while y <= len(data):
        if x + slope_x > 30:
            x += slope_x
            x = abs(31 - x)
        else: x += slope_x
        y += slope_y
        try: l.append(input[(x, y)])
        except: return l
    return l

data_new = convert_to_dict()

solution_1 = get_solution_slope(data_new, 1, 1)
solution_2 = get_solution_slope(data_new, 5, 1)
solution_3 = get_solution_slope(data_new, 7, 1)
solution_4 = get_solution_slope(data_new, 1, 2)
e = get_solution(data_new)

len_1 = len([i for i in solution_1 if i == "#"])
len_2 = len([i for i in solution_2 if i == "#"])
len_3 = len([i for i in solution_3 if i == "#"])
len_4 = len([i for i in solution_4 if i == "#"])
len_e = len([i for i in e if i == "#"])

print(len_1 * len_2 * len_3 * len_4 * len_e)

#print(len([i for i in e if i == "#"]))