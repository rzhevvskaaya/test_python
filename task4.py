
def sort_strings_by_length(input_list):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) > len(input_list[j]):
                input_list[i], input_list[j] = input_list[j], input_list[i]

    sorted_list_asc = input_list.copy()

    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) < len(input_list[j]):
                input_list[i], input_list[j] = input_list[j], input_list[i]

    sorted_list_desc = input_list

    return sorted_list_asc, sorted_list_desc


# Пример использования программы
input_list = ["cat", "turtle", "hamster", "fish", "chinchilla"]
sorted_asc, sorted_desc = sort_strings_by_length(input_list)

print(sorted_asc)
print(sorted_desc)
