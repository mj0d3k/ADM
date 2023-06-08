def format_list_right(input_list):
    formatted_string = ""
    max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
    #print(max_lengths)
    dlugosc = len(input_list)
    indeks = 1
    formatted_string += "["
    for row in input_list:
        formatted_string += "["
        for i, num in enumerate(row):
            cos = ","
            #formatted_string += str(num)
            #formatted_string += f"{str(num):<{max_lengths[i]}}"
            #fmt = '{:<' + f'{max_lengths[i]+1}' + '}'
            #formatted_string += fmt.format(str(num) + ',')
            if i != len(row) - 1:
                fmt = '{:<' + f'{max_lengths[i]+1}' + '}'
                formatted_string += fmt.format(str(num) + ',')
                formatted_string += " "
            else:
                formatted_string += f"{str(num):<{max_lengths[i]}}"
        #formatted_string = formatted_string[:-1]
        if indeks != dlugosc:
            formatted_string += "],\n "
        else:
            formatted_string += "]]"
        indeks+=1
    return formatted_string

input_list = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
formatted_string = format_list_right(input_list)
print(formatted_string)