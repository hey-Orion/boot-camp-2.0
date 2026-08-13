def get_even_num(numbers: list[int]) -> list[int]:
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    return evens

def count_occurrences(names: list[str]) -> dict[str, int]:
    counts = {}

    for name in names:
        counts[name] = counts.get(name, 0) + 1 

    return counts

def sum_key_values(dict_list: list[dict], target_key: str) -> int:
    total = 0
    for item in dict_list:
        if target_key in item:
            total += item[target_key]

    return total

def removes_duplicate(ex_list: list[int]) -> list[int]:
    cleand = []

    for item in ex_list:
        if item not in cleand:
            cleand.append(item)

    return cleand

def reverse_str(hada: str) -> str:
    return hada[::-1]