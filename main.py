
# moduł A lewa strona
def format_list_right(l: list) -> str:
    output = ""
    max_lengths = [max(map(len, map(str, col))) for col in zip(*l)]
    dlugosc = len(l)
    indeks = 1
    output += "["
    for row in l:
        output += "["
        for i, num in enumerate(row):
            output += f"{str(num):>{max_lengths[i]}}"
            if i != len(row) - 1:
                output += ", "
        if indeks != dlugosc:
            output += "],\n "
        else:
            output += "]]"
        indeks += 1
    return output


def format_list_left(input_list):
    formatted_string = ""
    max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
    dlugosc = len(input_list)
    indeks = 1
    formatted_string += "["
    for row in input_list:
        formatted_string += "["
        for i, num in enumerate(row):
            if i + 1 != len(row):
                formatted_string += f"{str(num) + ', ':<{max_lengths[i] + 2}}"
            elif i + 1 == len(row):
                formatted_string += f"{str(num):<{max_lengths[i]}}"
        if indeks != dlugosc:
            formatted_string += "],\n "
        else:
            formatted_string += "]]"
        indeks += 1
    return formatted_string

l = [[1, 2, 10, 150], [10, 2, 2, 2], [1, 120, 1, 100]]
output = format_list_right(l)
print(output)

# testy

example = [[19900, 5, 120, 1150], [155, 1, 12000, 8992], [3, 12, 455, 100]]
result = """[[19900,  5,   120, 1150],
 [  155,  1, 12000, 8992],
 [    3, 12,   455,  100]]"""
assert format_list_right(example) == result

example = [[656, 231, 231, 50], [1445, 6, 121, 992]]
result = """[[ 656, 231, 231,  50],
 [1445,   6, 121, 992]]"""
assert format_list_right(example) == result

example = [[656, 231, 231, 50], [1445, 6, 1, 992], [12132, 6, 242334, 992], [76, 6, 2, 992]]
result = """[[  656, 231,    231,  50],
 [ 1445,   6,      1, 992],
 [12132,   6, 242334, 992],
 [   76,   6,      2, 992]]"""
assert format_list_right(example) == result


