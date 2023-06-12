import math

def find_square_vertex(lista):
    p12 = math.sqrt(((lista[1][0] - lista[0][0]) ** 2) + (lista[1][1] - lista[0][1]) ** 2)
    p13 = math.sqrt(((lista[2][0] - lista[0][0]) ** 2) + (lista[2][1] - lista[0][1]) ** 2)
    p23 = math.sqrt(((lista[1][0] - lista[2][0]) ** 2) + (lista[1][1] - lista[2][1]) ** 2)
    P1 = []
    P2 = []
    P3 = []
    P4 = [0, 0]
    if p12 > p13 and p12 > p23:
        P1 = lista[2]
        P2 = lista[0]
        P3 = lista[1]
    elif p13 > p12 and p13 > p23:
        P1 = lista[1]
        P2 = lista[0]
        P3 = lista[2]
    else:
        P1 = lista[0]
        P2 = lista[1]
        P3 = lista[2]

    indeks1 = P2[0] + P3[0] - P1[0]
    indeks2 = P2[1] + P3[1] - P1[1]
    P4[0] = indeks1
    P4[1] = indeks2

    # d = {'p12': p12, 'p13':p13}

    return P4


print(find_square_vertex([[1, 1], [2, 3], [4, 2]]))


def find_triangle_vertex(lista):
    x3v1=(lista[0][0] + lista[1][0] + math.sqrt(3)*(lista[0][1]-lista[1][1]))/2
    y3v1=(lista[0][1] + lista[1][1] + math.sqrt(3)*(lista[1][0] - lista[0][0]))/2
    x3v2=(lista[0][0] + lista[1][0] + math.sqrt(3)*(lista[1][1]-lista[0][1]))/2
    y3v2=(lista[0][1] + lista[1][1] + math.sqrt(3)*(lista[0][0] - lista[1][0]))/2

    return [[x3v1,y3v1],[x3v2,y3v2]]
print(find_triangle_vertex([[0,0], [2,0]]))
#v3 = ( (x1 + x2 + Sqrt[3] (y1 - y2) )/2, (y1 + y2 + Sqrt[3] (x2 - x1) )/2).
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


l = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
output = format_list_left(l)
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

example = [[19900, 5, 120, 1150], [155, 1, 12000, 8992], [3, 12, 455, 100]]
result = """[[19900, 5,  120,   1150],
 [155,   1,  12000, 8992],
 [3,     12, 455,   100 ]]"""
assert format_list_left(example) == result

example = [[656, 231, 231, 50], [1445, 6, 121, 992]]
result = """[[656,  231, 231, 50 ],
 [1445, 6,   121, 992]]"""
assert format_list_left(example) == result

example = [[656, 231, 231, 50], [1445, 6, 1, 992], [12132, 6, 242334, 992], [76, 6, 2, 992]]
result = """[[656,   231, 231,    50 ],
 [1445,  6,   1,      992],
 [12132, 6,   242334, 992],
 [76,    6,   2,      992]]"""
assert format_list_left(example) == result

example = [[1, 1], [4, 4], [4, 1]]
result = [1, 4]
assert find_square_vertex(example) == result

example = [[5, 1], [6, -1], [3, 0]]
result = [4, -2]
assert find_square_vertex(example) == result

example = [[-2, 1], [1, 4], [1, -2]]
result = [4, 1]
assert find_square_vertex(example) == result
