


#print("[", end="")
#for x in range(len(lista)):
    #if x == len(lista)-1:
      #  print(lista[x])
    #elif:
    #    datasizemask
    #else:
     #   pr
#print("]")

def format_list(input_list):
    formatted_string = ""
    max_lengths = [max(map(len, map(str, col))) for col in zip(*input_list)]
    formatted_string= formatted_string
    for row in input_list:
        formatted_string += "["
        for i, num in enumerate(row):
            formatted_string += f"{str(num):>{max_lengths[i]}}"
            if i != len(row) - 1:
                formatted_string += ", "
        formatted_string += "]\n "
    
    return formatted_string
input_list = [[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]]
formatted_string = format_list(input_list)
print(formatted_string)

[[1,  2,   10,   150],
 [10, 2,   1000, 2],
 [1,  120, 1,    1000]]