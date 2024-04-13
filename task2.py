import math

def is_simple(var: int) -> bool:
    if var < 2:
        return False
    for i in range(2, int(math.sqrt(var)) + 1):
        if var % i == 0:
            return False
    return True

def simple_array(min: int, max: int) -> list:
    return [var for var in range(min, max + 1) if is_simple(var)]

# Пример использования программы
print(simple_array(1, 76))