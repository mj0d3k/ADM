def format_list_right(input_list):
    formatted_string = ""
    max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
    dlugosc = len(input_list)
    indeks = 1
    formatted_string += "["
    for row in input_list:
        formatted_string += "["
        for i, num in enumerate(row):
            formatted_string += f"{str(num):<{max_lengths[i]}}"
            if i != len(row) - 1:
                formatted_string += ", "
        if indeks != dlugosc:
            formatted_string += "],\n "
        else:
            formatted_string += "]]"
        indeks+=1
    return formatted_string

input_list = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
formatted_string = format_list_right(input_list)
print(formatted_string)