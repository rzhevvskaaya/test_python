def unique_elements(input_list: list) -> list:
    """
    Версия 1
    input_list: переданный список значений
    return: лист уникальных значений
    """
    return list(set(input_list))


def find_unique_element(input_list: list) -> list:
    """
    Версия 2
    input_list: переданный список значений
    unique_list: лист с уникальнми значениями
    return: unique_list
    """
    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


# Пример использования функции
input_list = [1, 2, 3, 5, 1, 4, 2, 4, 5, 1, 6, 7, 7]
result = find_unique_element(input_list)
print(result)
